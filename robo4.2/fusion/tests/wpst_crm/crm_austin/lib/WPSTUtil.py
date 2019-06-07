import sys
import json
import re
import os
import types
import imp
import copy
import gc
from time import (sleep, strftime)
from RoboGalaxyLibrary.utilitylib import logging as logger
from tests.wpst_crm.crm_austin.lib.mrgvirtualconnect import VirtualConnect
from tests.wpst_crm.crm_austin.lib.vcutils import JsonData, JsonDiff, selectDataDiff
from WPSTResourceTools import (WPSTResourceTools, WPSTConnectionTemplate, WPSTConnections, WPSTLogicalInterconnectGroup)
from WPSTResourceTools import WPSTTaskStatistics
from WPSTResourceTools import EmailClient
from mrgvcinterface import Interface
from oamodule import InterconnectsBase


class WPSTUtil(object):

    def wpst_configure_vc(self, vc_credentials, oa_credentials, config=None, import_domain=True, verbose=True, checkvcmMode=True, doubleDense=False):
        try:
            if checkvcmMode is True:
                vcm_mode_output = self.wpst_execute_oacli_command(oa_credentials, 'show vcmode')
                vcm_mode_status = re.search(r"Virtual Connect Mode:\s(.*)", vcm_mode_output)
                vcm_primary_ip = vc_credentials['vcmIpAddress']

                if vcm_mode_status.group(1) == "Disabled":
                    logger.info("VC Mode is in \"Disabled state\", will now proceed with configuring VC...")
                elif vcm_mode_status.group(1) == "Enabled":
                    vcm_mode_ip = re.search(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', vcm_mode_output)
                    vcm_mode_domain = re.search(r"Virtual Connect Domain Name:\s(.*)", vcm_mode_output)

                    if vcm_mode_ip.group() == vcm_primary_ip:
                        logger.info("VC Mode is in \"Enabled\" state and primary VC module is in the expected IP (%s), will now proceed with configuring VC" % vcm_primary_ip)
                    else:
                        logger.info("The VC is managed by either unexpected VC/OV/VCEM or Secondary VC having IP address %s with VCM domain name as %s." % (vcm_mode_ip.group(), vcm_mode_domain.group(1)))
                        logger.info("Will not configure VC in this state, stopping the test now...")
                        errMsg = '[%s] The VC is managed by either unexpected VC/OV/VCEM or Secondary VC having IP address %s with VCM domain name as %s.' % (__file__, vcm_mode_ip.group(), vcm_mode_domain.group(1))
                        raise RuntimeError(errMsg)
                else:
                    logger.info("The VC is in unexpected state.")
                    logger.info("Stopping the test execution.")
                    errMsg = '[%s] The VC is in unexpected state' % (__file__)
                    raise RuntimeError(errMsg)
            """Configuring VC"""
            logger.info("Configuring VC...")
            virtualConnect = VirtualConnect(vc_credentials, oa_credentials)
            virtualConnect.config_virtual_connect(config, import_domain, verbose, doubleDense)

        except Exception, e:
            logger.info("Attempt to configure VC failed!")
            raise RuntimeError("Attempt to configure VC failed!", e)

    def wpst_delete_domain_vc(self, vc_credentials, oa_credentials, waitTime=120):
        virtualConnect = VirtualConnect(vc_credentials, oa_credentials)
        virtualConnect.delete_domain(waitTime)

    def wpst_clear_vc_mode(self, vc_credentials, oa_credentials):
        virtualConnect = VirtualConnect(vc_credentials, oa_credentials)
        virtualConnect.clear_vc_mode(oa_credentials)

    def wpst_execute_oacli_command(self, oa_credentials, cmd):
        root_credentials = {'ipAddress': oa_credentials['oaIpAddress'], 'username': oa_credentials['oaUsername'], 'password': oa_credentials['oaPassword']}
        _interface = Interface(root_credentials)
        oacli_output = _interface.send_command_wait(cmd)
        logger.info("%s output:" % cmd)
        logger.info(oacli_output)
        return oacli_output

    def wpst_reset_vc(self, vc_credentials, oa_credentials):
        virtualConnect = VirtualConnect(vc_credentials, oa_credentials)
        virtualConnect.reset_virtual_connect(oa_credentials)

    def wpst_restart_interconnect(self, vc_credentials, oa_credentials, bay):
        virtualConnect = VirtualConnect(vc_credentials, oa_credentials)
        virtualConnect.restart_interconnect_module(oa_credentials, bay)

    def wpst_remove_vc(self, vc_credentials, oa_credentials, bay):
        virtualConnect = VirtualConnect(vc_credentials, oa_credentials)
        virtualConnect.remove_virtual_connect(oa_credentials, bay)

    def wpst_show_interconnect(self, vc_credentials, oa_credentials, bayNumber):
        virtualConnect = VirtualConnect(vc_credentials, oa_credentials)
        return virtualConnect.show_interconnect_module(bayNumber)

    def wpst_check_no_comm_status(self, vc_credentials, oa_credentials, bayNumber):
        """ This is to detect an issue described in QXCR1001467844: Utah module in No Comm state after import enclosure """
        output = self.wpst_show_interconnect(vc_credentials, oa_credentials, bayNumber)
        for line in output:
            if line.split(':')[0].rstrip() == 'Status':
                if line.split(':')[1].lstrip() == 'No Comm':
                    return True
                else:
                    return False
        logger.info("[WARN] Status of interconnect in bay %s not known." % bayNumber)
        return False

    def wpst_execute_diag_command(self, oa_credentials, cmd, maxRetry=1):
        oa_credentials['ipAddress'] = oa_credentials['oaIpAddress']
        oa_credentials['username'] = oa_credentials['oaUsername']
        oa_credentials['password'] = oa_credentials['oaPassword']
        self.interconnect = InterconnectsBase(oa_credentials['username'], oa_credentials['ipAddress'], oa_credentials['password'])

        logger.info("Executing OA diag command %s  " % cmd)
        self.interconnect.execute_diag_cmd(cmd, maxRetry)
        logger.info("%s complete." % cmd)

    def wpst_generate_migrate_task_statistics(self, taskTree, taskGroupSN, taskGroupLN, filename, datafiledir):
        self.wpst_check_dataFiles_dir_exist(datafiledir)
        if not re.search('/', filename):
            filename = datafiledir + '/' + filename
        taskStatistics = WPSTTaskStatistics(taskGroupSN, taskGroupLN)
        return taskStatistics.generateMigrateTaskStatistics(taskTree, filename)

    def wpst_write_json(self, data, filename, datafiledir, filemode='w'):
        self.wpst_check_dataFiles_dir_exist(datafiledir)
        if not re.search('/', filename):
            filename = datafiledir + '/' + filename
        jsonData = JsonData()
        jsonData.write(data, filename, filemode)

    def wpst_convert_json_ignore(self, oldFile, newFile):
        jsonData = JsonData()
        jsonData.filter(oldFile, newFile)

    def wpst_compare_data(self, saveFile, runFile, datafiledir):
        jsonData = JsonData()
        saveFile = datafiledir + saveFile
        runFile = datafiledir + runFile
        return jsonData.compare(saveFile, runFile)

    def chunkList(self, lst, num):
        """ Create num-sized chunks of lst
        :param lst: list
        :param num: number of elments per list
        :return: tuple
        """
        return tuple(lst[i:i + num] for i in xrange(0, len(lst), num))

    def splitList(self, lst, num=1):
        """ Split the list into num list
        :param lst: list
        :param num: number of lists
        :return: list of lists
        """
        length = len(lst)
        return [lst[i * length / num:(i + 1) * length / num] for i in xrange(num)]

    def wpst_select_data_compare(self, compareFile, variableFile, reportFile, dataFileDir, resourceType="ALL", preserveDataFile=False):
        """ Compare Json files filter by resourceType.
            [Arguments]
            compareFile: saved JSON file (compare file)
            variableFile: variable file (resource data file to be compared)
            reportFile: select data compare report file
            dataFileDir: datafile directory
            resourceType: one of resource types (see resources/keywords.txt AllResourcesList variable for the list of valid names. Default: ALL)
        """
        report = []
        compareFile = dataFileDir + '/' + compareFile
        variableFile = dataFileDir + '/' + variableFile

        # print 'DEBUG: compareFile: %s' % compareFile
        # print 'DEBUG: variableFile: %s' % variableFile
        with open(compareFile, 'r+') as savefp:
            try:
                if resourceType == 'ALL' or resType == '*':
                    print "Running query on all supported resource types:"
                    savedData = json.load(savefp)
                else:
                    print "Running query on the following resource types: [%s]" % resourceType
                    savedData = json.load(savefp)[resourceType]
            except:
                e = sys.exc_info()[1]
                errorString = "Error is %s" % e
                print errorString
        # print 'DEBUG: savedData: %s' % savedData

        variableFileData = imp.load_source('variableFileData', variableFile)
        for k, v in variableFileData.default_variables.items():
            # print 'DEBUG: k: %s' % k
            # print 'DEBUG: v: %s' % v
            diff = selectDataDiff()
            if k == 'compatibility':
                diff.diff_data(savedData, v)
            else:
                diff.diff_data(savedData[k]['members'], v)

            # print 'DEBUG: diff: %s' % diff
            # print 'DBUG: diff.difference: %s' % diff.difference
            if len(diff.difference) > 0:
                logger._log_to_console_and_log_file('\nCurrent OneView data file: %s' % variableFile)
                logger._log_to_console_and_log_file('OneView compare file: %s' % compareFile)
                logger._log_to_console_and_log_file('Select data compare result: Differ')
                logger._log_to_console_and_log_file('\nPrinting the diff...')
                for di in diff.difference:
                    logger._log_to_console_and_log_file(''.join(di))
                    logger._log_to_console_and_log_file('')
                logger._log_to_console_and_log_file('\nFor debugging, keeping the current OneView data file %s...' % variableFile)
                logger._log_to_console_and_log_file('\nNOTE: You have to manually delete this file!\n')
                return False
            else:
                logger._log_to_console_and_log_file('\nCurrent OneView data file: %s' % variableFile)
                logger._log_to_console_and_log_file('OneView compare file: %s' % compareFile)
                logger._log_to_console_and_log_file('Select data compare result: Same')
                # Passed the select data compare. Delete the variable file.
                logger._log_to_console_and_log_file('\nRemoving the current OneView data file %s...' % variableFile)
                if preserveDataFile is False:
                    try:
                        os.remove(variableFile)
                        logger._log_to_console_and_log_file('%s successfully removed.\n' % variableFile)
                        logger._log_to_console_and_log_file('\nNOTE: To preserve the data file, use preserveDataFile argument.\n')
                    except OSError, e:
                        logger._log_to_console_and_log_file("\nError: %s - %s.\n" % (e.variableFile, e.strerror))
                else:
                    logger._log_to_console_and_log_file('\npreserveDataFile argument is True, keeping the current OneView data file: %s.\n' % variableFile)
                return True

    def wpst_diff_json(self, jsonfile1, jsonfile2, datafiledir, resType="ALL", excList=[], conditionalExcL=[], resolve_name=False):
        """ Compare Json files filter by resType and excludeList.
            [Arguments]
            jsonfile1: saved JSON file (compare file)
            jsonfile2: newly generated JSON file (file to be compared)
            datafiledir: datafile directory
            resType: one of resource types (ethNets, fcNets, lig, networkset, profiles, uplinkset)
            excList: list of attributes to be ignored during comparison
            conditionalExcL: list of dictionary containing conditionally excluded attribute(s)
        """
        diffs = []
        if not re.search('/', jsonfile1):
            jsonfile1 = datafiledir + '/' + jsonfile1
        if not re.search('/', jsonfile2):
            jsonfile2 = datafiledir + '/' + jsonfile2

        with open(jsonfile1, 'r+') as savefp, open(jsonfile2, 'r+') as runfp:
            try:
                if resType == 'ALL' or resType == '*':
                    print "Comparing all json content"
                    expectData = json.load(savefp)
                    actualData = json.load(runfp)
                else:
                    print "Comparing json content of %s resource" % resType
                    expectData = json.load(savefp)[resType]
                    actualData = json.load(runfp)[resType]

            except:
                e = sys.exc_info()[1]
                errorString = "Error is %s" % e
                print errorString
            taggedKeys_pathDataDict = {}
            for exclDict in conditionalExcL:
                taggedKeys = exclDict.get('taggedKeys')
                taggedKeys_path = exclDict.get('taggedKeys_path')
                if taggedKeys is not None:
                    try:
                        if taggedKeys_path is None or not re.search('.', taggedKeys_path):
                            errMsg = '[%s] Conditional exclusion "taggedKeys_path" attribute is %s: set it to valid "path"' % (__file__, taggedKeys_path)
                            raise RuntimeError(errMsg)
                        else:
                            # step-thru the taggedKeys_path in struct_pristine and get the value we want to search with
                            taggedKeys_pathList = taggedKeys_path.split('.')
                            if taggedKeys_pathList[1] != '':
                                taggedKeys_pathData = copy.deepcopy(actualData.get(taggedKeys_pathList[1]))
                                if taggedKeys_pathData is None:
                                    continue
                                taggedKeys_pathList.remove(taggedKeys_pathList[0])
                                taggedKeys_pathList.remove(taggedKeys_pathList[0])
                                breakit = False
                                for i in taggedKeys_pathList:
                                    if re.search('.*\[\*\]', i):
                                        i = re.sub('\[\*\]', '', i)
                                        breakit = True
                                    taggedKeys_pathData = taggedKeys_pathData[i]
                                    if breakit:
                                        break
                                taggedKeys_pathData = self.splitList(taggedKeys_pathData, 4)
                                taggedKeys_pathDataDict[taggedKeys_path] = taggedKeys_pathData
                            else:
                                taggedKeys_pathDataDict[taggedKeys_path] = actualData
                    except Exception as e:
                        raise Exception(e)
            diff = JsonDiff(conditionalExcL, taggedKeys_pathDataDict)
            diff.diff_structs(expectData, actualData, excList, resolve_name=resolve_name)

        if len(diff.difference) > 0:
            logger._log_to_console_and_log_file('\nCurrent OneView data file: %s' % jsonfile2)
            logger._log_to_console_and_log_file('Expected OneView data file: %s' % jsonfile1)
            logger._log_to_console_and_log_file('JSON compare result: Differ')
            logger._log_to_console_and_log_file('\nPrinting the diff...')
            for di in diff.difference:
                newline = ''.join(di) + '\r\n'
                logger._log_to_console_and_log_file(''.join(di))
            logger._log_to_console_and_log_file('')
            return False
        else:
            logger._log_to_console_and_log_file('\nCurrent OneView data file: %s' % jsonfile2)
            logger._log_to_console_and_log_file('Expected OneView data file: %s' % jsonfile1)
            logger._log_to_console_and_log_file('JSON compare result: Same')
            return True

    def wpst_add_ethnets_items(self, ip, sessionId, resourceData, api=None, headers=None):
        """ Add missing item to the resourceData
            [Arguments]
            ip - OV IP
            sessionId - OV session Id
            resourceData - dictionary of resource data
            [Return]
            updated/modified resourceData
        """

        connTempKW = WPSTConnectionTemplate()
        for members in resourceData['members']:
            membersUri = '%s/%s' % (ip, members['connectionTemplateUri'])
            connResponse = connTempKW.wpst_get_connection_templates(sessionId, uri=membersUri)
            members['connectionTemplateUri_ADD'] = connResponse

        return resourceData

    def wpst_add_fcnets_items(self, ip, sessionId, resourceData, api=None, headers=None):
        """ Add missing item to the resourceData
            [NOTES]
            Since this shares the same code as wpst_add_ethnets_items at the moment, we can just alias/wrap that one up.
            [Arguments]
            ip - OV IP
            sessionId - OV session Id
            resourceData - dictionary of resource data
            [Return]
            updated/modified resourceData
        """

        return self.wpst_add_ethnets_items(ip, sessionId, resourceData, api, headers)

    def wpst_add_fcoenets_items(self, ip, sessionId, resourceData, api=None, headers=None):
        """ Add missing item to the resourceData
            [NOTES]
            Since this shares the same code as wpst_add_ethnets_items at the moment, we can just alias/wrap that one up.
            [Arguments]
            ip - OV IP
            sessionId - OV session Id
            resourceData - dictionary of resource data
            [Return]
            updated/modified resourceData
        """

        return self.wpst_add_ethnets_items(ip, sessionId, resourceData, api, headers)

    def wpst_add_networkset_items(self, ip, sessionId, resourceData, api=None, headers=None):
        """ Add missing item to the resourceData
            [Arguments]
            ip - OV IP
            sessionId - OV session Id
            resourceData - dictionary of resource data
            [Return]
            updated/modified resourceData
        """

        for members in resourceData['members']:
            members['networkUris_ADD'] = self.create_list_of_uris(ip, sessionId, members, 'networkUris', api=api, headers=headers)

        return resourceData

    def wpst_add_uplinkset_items(self, ip, sessionId, resourceData, api=None, headers=None, tbirdEnv=False):
        """ Add missing item to the resourceData
            [Arguments]
            ip - OV IP
            sessionId - OV session Id
            resourceData - dictionary of resource data
            [Return]
            updated/modified resourceData
        """
        listOfKeys = ['networkUris', 'fcNetworkUris']

        resourceTools = WPSTConnections()
        for members in resourceData['members']:
            for theUri in listOfKeys:
                members[theUri + '_ADD'] = self.create_list_of_uris(ip, sessionId, members, theUri, api=api, headers=headers)

            for portConfigInfos in members['portConfigInfos']:
                bayId = ''
                portId = ''
                for locationEntries in portConfigInfos['location']['locationEntries']:
                    if locationEntries['type'] == 'Bay':
                        bayId = locationEntries['value']
                    elif locationEntries['type'] == 'Port':
                        portId = locationEntries['value']
                portConfigInfos['Location_ADD'] = 'Bay%s: Port%s' % (bayId, portId)
                if 'portUri' in portConfigInfos:
                    response = resourceTools.get_all_by_uri(ip, sessionId, portConfigInfos['portUri'], api=api, headers=headers)
                    portConfigInfos['portUri_ADD'] = response

        return resourceData

    def wpst_add_lig_items(self, ip, sessionId, resourceData, api=None, headers=None):
        """ Add missing item to the resourceData
            [Arguments]
            ip - OV IP
            sessionId - OV session Id
            resourceData - dictionary of resource data
            [Return]
            updated/modified resourceData
        """

        resourceTools = WPSTConnections()
        for members in resourceData['members']:
            for interconnectMapEntryTemplates in members['interconnectMapTemplate']['interconnectMapEntryTemplates']:
                if interconnectMapEntryTemplates['permittedInterconnectTypeUri'] is not None:
                    response = resourceTools.get_attr_by_uri(ip, sessionId, interconnectMapEntryTemplates['permittedInterconnectTypeUri'], api=api, headers=headers)
                    interconnectMapEntryTemplates['permittedInterconnectType_ADD'] = response
                encId = ''
                bayId = ''
                for locationEntries in interconnectMapEntryTemplates['logicalLocation']['locationEntries']:
                    if locationEntries['type'] == 'Enclosure':
                        encId = locationEntries['relativeValue']
                    elif locationEntries['type'] == 'Bay':
                        bayId = locationEntries['relativeValue']
                interconnectMapEntryTemplates['logicalLocation_ADD'] = 'Enc%s: Bay%s' % (encId, bayId)

            for uplinkSets in members['uplinkSets']:
                encId = ''
                bayId = ''
                portId = ''
                responseNameList = []
                for logicalPortConfigInfos in uplinkSets['logicalPortConfigInfos']:
                    for locationEntries in logicalPortConfigInfos['logicalLocation']['locationEntries']:
                        if locationEntries['type'] == 'Bay':
                            bayId = locationEntries['relativeValue']
                        elif locationEntries['type'] == 'Port':
                            portId = locationEntries['relativeValue']
                        elif locationEntries['type'] == 'Enclosure':
                            encId = locationEntries['relativeValue']
                    logicalPortConfigInfos['logicalLocation_ADD'] = 'Enc%s: Bay%s: Port%s' % (encId, bayId, portId)

                for networkUris in uplinkSets['networkUris']:
                    responseNameList.append(resourceTools.get_attr_by_uri(ip, sessionId, networkUris, api=api, headers=headers))
                uplinkSets['networkUris_ADD'] = responseNameList

        return resourceData

    def wpst_add_li_items(self, ip, sessionId, resourceData, api=None, headers=None, tbirdEnv=False):
        """ Add missing item to the li resourceData
            [Arguments]
            ip - OV IP
            sessionId - OV session Id
            resourceData - dictionary of resource data
            [Return]
            updated/modified resourceData
        """
        # TODO: take this out off this code and place somewhere easy for users to update as things change moving forward
        # group for uris under members that we need to parse
        # list of uris to access off resourceData['members']
        membersUriList = ['enclosureUris', 'logicalInterconnectGroupUri', 'interconnects']

        # list of attributes we get off enclosureUris
        enclosureUrisAttrList = [
            'serialNumber', 'uuid', 'assetTag', 'enclosureType', 'rackName', 'deviceBayCount', 'oaBayCount', 'activeOaPreferredIP',
            'standbyOaPreferredIP', 'isFWManaged', 'fwBaseline', 'vcMode', 'vcmUrl', 'vcmDomainName', 'vcmDomainId', 'licensingIntent',
            'name', 'refreshState', 'status', 'state', 'stateReason', 'deviceBays', 'oa'
        ]
        # this is a subset of enclosureUrisAttrList listing dictionary keys
        enclosureUrisDictKeyList = ['deviceBays', 'oa']
        enclosureUrisDictKeyListAttr = {
            enclosureUrisDictKeyList[0]: ['bayNumber', 'devicePresence', 'availableForFullHeightProfile', 'availableForHalfHeightProfile'],
            enclosureUrisDictKeyList[1]: ['bayNumber', 'fwVersion', 'role', 'ipAddress', 'fwBuildDate', 'fqdnHostName', 'dhcpEnable', 'dhcpIpv6Enable', 'state']
        }

        # list of attributes we get off logicalInterconnectGroupUri
        logicalInterconnectGroupUriAttrList = ['name']

        # list of attributes to get for interconnects
        interconnectsAttrList = [
            'name', 'model', 'productName', 'firmwareVersion', 'powerStatus', 'portCount', 'partNumber', 'igmpIdleTimeoutInterval', 'enclosureName',
            'interconnectIP', 'enableIgmpSnooping', 'networkLoopProtectionInterval', 'enableNetworkLoopProtection', 'enableFastMacCacheFailover',
            'maxBandwidth', 'subPortCount', 'edgeVirtualBridgingAvailable', 'serialNumber', 'status', 'state', 'ports'
        ]
        # interconnectsAttrList list of dictionary keys we are interested of (subset of interconnectsAttrList
        interconnectsDictKeyList = ['ports']
        interconnectsDictKeyListAttr = {
            interconnectsDictKeyList[0]: [
                'lagId', 'portStatus', 'portName', 'interconnectName', 'bayNumber', 'portType', 'portHealthStatus',
                'enabled', 'portMonitorConfigInfo', 'portId', 'subports', 'connectorType', 'associatedUplinkSetObjectId', 'portTypeExtended',
                'operationalSpeed', 'status'
            ]
        }

        # define dict for all the uris we are interested
        membersUriDict = {
            membersUriList[0] + 'AttrList': enclosureUrisAttrList,
            membersUriList[0] + 'DictKeyList': enclosureUrisDictKeyList,
            membersUriList[0] + 'DictKeyListAttr': enclosureUrisDictKeyListAttr,
            membersUriList[1] + 'AttrList': logicalInterconnectGroupUriAttrList,
            membersUriList[1] + 'DictKeyList': [],
            membersUriList[1] + 'DictKeyListAttr': {},
            membersUriList[2] + 'AttrList': interconnectsAttrList,
            membersUriList[2] + 'DictKeyList': interconnectsDictKeyList,
            membersUriList[2] + 'DictKeyListAttr': interconnectsDictKeyListAttr,
        }

        # group for dict keys with dict of list values we needed to parse
        # list of dict key of dict of list value that we are interested to parse
        membersDictOfList = ['interconnectMap']
        # list of keys under membersDictOfList
        interconnectMapList = ['interconnectMapEntries']
        # list of uris to follow
        interconnectMapEntriesUri = ['permittedInterconnectTypeUri']

        # attribute to get from Uri
        permittedInterconnectTypeUriAttrList = ['partNumber', 'minimumFirmwareVersion', 'maximumFirmwareVersion', 'portInfos', 'name', 'downlinkCapabilities', 'downlinkCount', 'status', 'state']
        # permittedInterconnectTypeUriAttrList list of dict keys we are interested of (subset of permittedInterconnectTypeUriAttrList)
        permittedInterconnectTypeUriDictKeyList = ['portInfos']
        permittedInterconnectTypeUriListList = ['downlinkCapabilities']
        permittedInterconnectTypeUriDictKeyListAttr = {
            permittedInterconnectTypeUriDictKeyList[0]: ['portName', 'portNumber', 'uplinkCapable', 'downlinkCapable']
        }
        # define members dict key with list in a dictionary value
        membersDictKey = {
            # define interconnectMap dict
            membersDictOfList[0] + 'MapList': interconnectMapList[0],
            interconnectMapEntriesUri[0] + 'AttrList': permittedInterconnectTypeUriAttrList,
            interconnectMapEntriesUri[0] + 'DictKeyList': permittedInterconnectTypeUriDictKeyList,
            interconnectMapEntriesUri[0] + 'DictKeyListAttr': permittedInterconnectTypeUriDictKeyListAttr,
            interconnectMapEntriesUri[0] + 'ListList': permittedInterconnectTypeUriListList
        }

        resourceTools = WPSTConnections()
        for members in resourceData['members']:
            for membersUri in membersUriList:
                if isinstance(members[membersUri], (str, unicode)):
                    members[membersUri] = [members[membersUri]]
                # grab the enclosureUris and loops thru it
                for enclosureUris in members[membersUri]:
                    enclosureUris = enclosureUris.encode('ascii', 'xmlcharrefreplace')
                    # get the attributes in the list
                    for enclosureUriAttr in membersUriDict[membersUri + 'AttrList']:
                        if tbirdEnv is True and enclosureUriAttr == 'oa':
                            continue
                        resourceToolsResponse = resourceTools.get_attr_by_uri(ip, sessionId, enclosureUris, attr=enclosureUriAttr, api=api, headers=headers)
                        # selected attribute is in the dictionary key listed enclosureUrisDictKeyList
                        if enclosureUriAttr in membersUriDict[membersUri + 'DictKeyList']:
                            # oa attribute has list value for older x-api-version. However, that attribute does not exists in x-api-version 300.
                            if resourceToolsResponse is None:
                                continue
                            # send individual data into resourceToolsResp dict from resourceToolsResponse list
                            count = 0
                            for resourceToolsResp in self.sortList(resourceToolsResponse, 'portName'):
                                # get value of a key in the enclosureUrisDictKeyListAttr
                                for listKey in self.sortList(membersUriDict[membersUri + 'DictKeyListAttr'][enclosureUriAttr], 'portName'):
                                    if ((tbirdEnv is True and listKey == 'associatedUplinkSetObjectId') or (listKey not in resourceToolsResp)):
                                        continue
                                    members[membersUri + '_ADD_' + enclosureUriAttr + '_' + str(count) + '_' + listKey] = resourceToolsResp[listKey]
                                count += 1
                        else:
                            members[membersUri + '_ADD_' + enclosureUriAttr] = resourceToolsResponse

            for membersDict in membersDictOfList:
                for interconnectMapEntries in members[membersDict][membersDictKey[membersDict + 'MapList']]:
                    for uriToFollow in interconnectMapEntriesUri:
                        for attrToGet in membersDictKey[uriToFollow + 'AttrList']:
                            if tbirdEnv is True and attrToGet == 'downlinkCapabilities':
                                continue
                            response = resourceTools.get_attr_by_uri(ip, sessionId, interconnectMapEntries[uriToFollow], attr=attrToGet, api=api, headers=headers)
                            if attrToGet in membersDictKey[uriToFollow + 'DictKeyList']:
                                count = 0
                                for resp in self.sortList(response, 'portName'):
                                    for listKey in self.sortList(membersDictKey[uriToFollow + 'DictKeyListAttr'][attrToGet], 'portName'):
                                        interconnectMapEntries[uriToFollow + '_ADD_' + attrToGet + '_' + str(count) + '_' + listKey] = resp[listKey]
                                    count += 1
                            elif attrToGet in membersDictKey[uriToFollow + 'ListList']:
                                if response is None:
                                    continue
                                count = 0
                                for resp in self.sortList(response, 'portName'):
                                    interconnectMapEntries[uriToFollow + '_ADD_' + attrToGet + '_' + str(count)] = resp
                                    count += 1
                            else:
                                interconnectMapEntries[uriToFollow + '_ADD_' + attrToGet] = response

                    encId = ''
                    bayId = ''
                    for locationEntries in interconnectMapEntries['location']['locationEntries']:
                        if locationEntries['type'] == 'Enclosure':
                            encId = resourceTools.get_attr_by_uri(ip, sessionId, locationEntries['value'], api=api, headers=headers)
                        elif locationEntries['type'] == 'Bay':
                            bayId = locationEntries['value']
                    interconnectMapEntries['location_ADD'] = 'Enc %s: Bay %s' % (encId, bayId)

        return resourceData

    def wpst_add_encgrp_items(self, ip, sessionId, resourceData, api=None, headers=None):
        """ Add missing item to the encgrp resourceData
            [Arguments]
            ip - OV IP
            sessionId - OV session Id
            resourceData - dictionary of resource data
            [Return]
            updated/modified resourceData
        """
        # TODO: We need to define what data we need that is not provided by resourceData already

        return resourceData

    def wpst_add_encs_items(self, ip, sessionId, resourceData, api=None, headers=None):
        """ Add missing item to the enclosures resourceData
            [Arguments]
            ip - OV IP
            sessionId - OV session Id
            resourceData - dictionary of resource data
            [Return]
            updated/modified resourceData
        """

        # mapping of variables
        # members key of list of dicts
        membersDictKey = ['deviceBays', 'interconnectBays']

        deviceBaysUris = ['deviceUri']
        interconnectBaysUris = ['interconnectUri']

        deviceUriAttr = [
            'name', 'state', 'stateReason', 'assetTag', 'formFactor', 'licensingIntent', 'memoryMb', 'model', 'mpDnsName', 'mpFirmwareVersion', 'mpIpAddress', 'mpModel',
            'partNumber', 'position', 'powerLock', 'powerState', 'processorCoreCount', 'processorCount', 'processorSpeedMhz', 'processorType', 'refreshState', 'romVersion',
            'serialNumber', 'shortModel', 'status'
        ]
        interconnectUriAttr = [
            'partNumber', 'ports', 'powerStatus', 'model', 'firmwareVersion', 'portCount', 'igmpIdleTimeoutInterval', 'enclosureName', 'productName', 'interconnectIP',
            'enableIgmpSnooping', 'networkLoopProtectionInterval', 'enableFastMacCacheFailover', 'maxBandwidth', 'subPortCount', 'edgeVirtualBridgingAvailable',
            'serialNumber', 'status', 'name', 'state'
        ]

        deviceUriDictKey = []
        # interconnectUri dict key
        interconnectUriDictKey = ['ports']

        interconnectUriDictKeyAttr = {
            interconnectUriDictKey[0]: [
                'lagId', 'portStatus', 'portName', 'interconnectName', 'bayNumber', 'portType', 'portHealthStatus',
                'enabled', 'portMonitorConfigInfo', 'portId', 'connectorType',
                'portTypeExtended', 'operationalSpeed', 'status', 'name', 'state'
            ]
        }

        membersUrisAttrDict = {
            # deviceBays
            membersDictKey[0] + 'Uris': deviceBaysUris,
            deviceBaysUris[0] + 'Attr': deviceUriAttr,
            deviceBaysUris[0] + 'DictKeyAttr': {},
            deviceBaysUris[0] + 'DictKey': deviceUriDictKey,
            # interconnect Bays
            membersDictKey[1] + 'Uris': interconnectBaysUris,
            interconnectBaysUris[0] + 'Attr': interconnectUriAttr,
            interconnectBaysUris[0] + 'DictKeyAttr': interconnectUriDictKeyAttr,
            interconnectBaysUris[0] + 'DictKey': interconnectUriDictKey
        }

        resourceTools = WPSTConnections()
        for members in resourceData['members']:
            for membersKey in membersDictKey:
                # loop membersDictKey value
                for membersDictKeyVal in members[membersKey]:
                    for uriName in membersUrisAttrDict[membersKey + 'Uris']:
                        if membersDictKeyVal[uriName] is None:
                            continue
                        for attrToGet in membersUrisAttrDict[uriName + 'Attr']:
                            response = resourceTools.get_attr_by_uri(ip, sessionId, membersDictKeyVal[uriName], attr=attrToGet, api=api, headers=headers)
                            # do something for the ones in *DictKey
                            if attrToGet in membersUrisAttrDict[uriName + 'DictKey']:
                                count = 0
                                for resp in self.sortList(response, 'portName'):
                                    for listKey in self.sortList(membersUrisAttrDict[uriName + 'DictKeyAttr'][attrToGet], 'portName'):
                                        membersDictKeyVal[uriName + '_ADD_' + attrToGet + '_' + str(count) + '_' + listKey] = resp[listKey]
                                    count += 1
                            else:
                                membersDictKeyVal[uriName + '_ADD_' + attrToGet] = response

        return resourceData

    def wpst_add_server_items(self, ip, sessionId, resourceData, api=None, headers=None):
        """ Add missing item to the server resourceData
            [Arguments]
            ip - OV IP
            sessionId - OV session Id
            resourceData - dictionary of resource data
            [Return]
            updated/modified resourceData
        """

        membersUri = ['serverGroupUri', 'serverHardwareTypeUri', 'serverProfileUri']

        serverGroupUriAttr = ['name', 'status', 'state', 'stackingMode', 'portMappingCount', 'interconnectBayMappingCount']
        serverHardwareTypeUriAttr = ['name', 'model', 'formFactor', 'biosSettings']
        if api >= 600:
            serverProfileUriAttr = ['name', 'description', 'serialNumber', 'enclosureBay', 'macType', 'wwnType', 'serialNumberType', 'status', 'state', 'inProgress', 'connectionSettings']
        else:
            serverProfileUriAttr = ['name', 'description', 'serialNumber', 'enclosureBay', 'macType', 'wwnType', 'serialNumberType', 'status', 'state', 'inProgress', 'connections']

        serverGroupUriDictKey = []
        serverHardwareTypeUriDictKey = []
        serverProfileUriDictKey = ['connections']

        serverGroupUriDictKeyAttr = {}
        serverHardwareTypeUriDictKeyAttr = {}
        if api >= 500:
            serverProfileUriDictKeyAttr = {
                serverProfileUriDictKey[0]: ['id', 'functionType', 'portId', 'macType', 'wwpnType', 'mac', 'wwnn', 'wwpn', 'requestedMbps', 'allocatedMbps', 'maximumMbps'],
            }
        else:
            serverProfileUriDictKeyAttr = {
                serverProfileUriDictKey[0]: ['id', 'functionType', 'deploymentStatus', 'portId', 'macType', 'wwpnType', 'mac', 'wwnn', 'wwpn', 'requestedMbps', 'allocatedMbps', 'maximumMbps'],
            }

        membersUriDict = {
            membersUri[0] + 'Attr': serverGroupUriAttr,
            membersUri[0] + 'DictKey': serverGroupUriDictKey,
            membersUri[0] + 'DictKeyAttr': serverGroupUriDictKeyAttr,
            membersUri[1] + 'Attr': serverHardwareTypeUriAttr,
            membersUri[1] + 'DictKey': serverHardwareTypeUriDictKey,
            membersUri[1] + 'DictKeyAttr': serverHardwareTypeUriDictKeyAttr,
            membersUri[2] + 'Attr': serverProfileUriAttr,
            membersUri[2] + 'DictKey': serverProfileUriDictKey,
            membersUri[2] + 'DictKeyAttr': serverProfileUriDictKeyAttr
        }

        resourceTools = WPSTConnections()
        for members in resourceData['members']:
            for uriName in membersUri:
                if isinstance(members[uriName], (str, unicode)):
                    members[uriName] = [members[uriName]]
                else:
                    continue
                for uriValue in members[uriName]:
                    uriValue = uriValue.encode('ascii', 'xmlcharrefreplace')
                    # get the attributes in the list
                    for uriAttr in membersUriDict[uriName + 'Attr']:
                        response = resourceTools.get_attr_by_uri(ip, sessionId, uriValue, attr=uriAttr, api=api, headers=headers)
                        if uriAttr in membersUriDict[uriName + 'DictKey']:
                            count = 0
                            for resp in self.sortList(response, 'portName'):
                                for listKey in self.sortList(membersUriDict[uriName + 'DictKeyAttr'][uriAttr], 'portName'):
                                    members[uriName + '_ADD_' + uriAttr + '_' + str(count) + '_' + listKey] = resp[listKey]
                                count += 1
                        else:
                            members[uriName + '_ADD_' + uriAttr] = response

        return resourceData

    def wpst_add_profiles_items(self, ip, sessionId, resourceData, api=None, headers=None):
        """ Add missing item to the resourceData
            [Arguments]
            ip - OV IP
            sessionId - OV session Id
            resourceData - dictionary of resource data
            [Return]
            updated/modified resourceData
        """

        resourceTools = WPSTConnections()
        for members in resourceData['members']:
            for connections in members['connectionSettings']['connections']:
                if connections['networkUri'] is not None:
                    connections['networkUri_ADD'] = resourceTools.get_attr_by_uri(ip, sessionId, connections['networkUri'], api=api, headers=headers)

        return resourceData

    def wpst_add_interconnect_items(self, ip, sessionId, resourceData, api=None, headers=None):
        """ Add missing item to the interconnect resourceData
            [Arguments]
            ip - OV IP
            sessionId - OV session Id
            resourceData - dictionary of resource data
            [Return]
            updated/modified resourceData
        """

        resourceTools = WPSTConnections()
        for members in resourceData['members']:
            encId = ''
            bayId = ''
            for locationEntries in members['interconnectLocation']['locationEntries']:
                if locationEntries['type'] == 'Enclosure':
                    encId = resourceTools.get_attr_by_uri(ip, sessionId, locationEntries['value'], api=api, headers=headers)
                elif locationEntries['type'] == 'Bay':
                    bayId = locationEntries['value']
            members['interconnectLocation']['locationEntries_ADD'] = 'Enc %s: Bay %s' % (encId, bayId)

        return resourceData

    def wpst_add_interconnecttype_items(self, ip, sessionId, resourceData, api=None, headers=None):
        """ Add missing item to the interconnect type resourceData
            [Arguments]
            ip - OV IP
            sessionId - OV session Id
            resourceData - dictionary of resource data
            [Return]
            updated/modified resourceData
        """

        return resourceData

    def wpst_add_interconnectstate_items(self, ip, sessionId, resourceData, api=None, headers=None):
        """ Add missing item to the interconnect type resourceData
            [Arguments]
            ip - OV IP
            sessionId - OV session Id
            resourceData - dictionary of resource data
            [Return]
            updated/modified resourceData
        """

        return resourceData

    def wpst_add_user_items(self, ip, sessionId, resourceData, api=None, headers=None):
        """ Add missing item to the interconnect type resourceData
            [Arguments]
            ip - OV IP
            sessionId - OV session Id
            resourceData - dictionary of resource data
            [Return]
            updated/modified resourceData
        """

        return resourceData

    def wpst_generate_compatibility_variable_file(self, resourceData, fileName, variableName, vMapFile='../resources/public/compatibility.conf', mode='write'):
        """ Compatibility report parser for variable file
            [Arguments]
            resourceData - dictionary of resource data
            fileName - file to save parsed data to
            variableName - variable name to use for the generated data file
            vMapFile - [optional] resource's variable-to-keys mapping
            mode - write or append to fileName
        """

        with open(vMapFile, 'r') as r:
            vConfig = imp.new_module('data')
            exec(r.read(), vConfig.__dict__)
        compatibility = vConfig.compatibility
        credentials = vConfig.credentials
        itemCount = vConfig.itemCount
        items = vConfig.items
        issues = vConfig.issues

        self.wpst_create_variable_file_header(fileName, mode)
        with open(fileName, 'a') as f:
            f.write(variableName + ' = {\n')
            for k, v in resourceData.iteritems():
                for c in compatibility:
                    if c == k:
                        # print 'DEBUG: key: %s' % k
                        if c in locals():
                            # print 'DEBUG: locals has: %s' % c
                            if isinstance(v, dict):
                                # print 'DEBUG: v is dict: %s' % v
                                f.write(' ' * 4 + '"' + k + '": ' + '{\n')
                                for i, (k1, v1) in self.wpst_annotate(v.iteritems()):
                                    # print 'DEBUG: v is dict: k1: %s, v1: %s' % (k1, v1)
                                    if k1 in eval(c) and i == '-1':
                                        f.write(' ' * 8 + '"' + k1 + '": ' + self._ascii_encode(v1) + '\n')
                                    elif k1 in eval(c):
                                        f.write(' ' * 8 + '"' + k1 + '": ' + self._ascii_encode(v1) + ',\n')
                                f.write(' ' * 4 + '},\n')
                            if isinstance(v, list):
                                # print 'DEBUG: v is list: %s' % v
                                f.write(' ' * 4 + '"' + k + '": ' + '[\n')
                                for l in v:
                                    if isinstance(l, dict):
                                        # print 'DEBUG: v is list: l is dict: %s' % l
                                        f.write(' ' * 8 + '{\n')
                                        for i, (k1, v1) in self.wpst_annotate(l.iteritems()):
                                            if k1 in eval(c) and i == '-1':
                                                f.write(' ' * 16 + '"' + k1 + '": ' + self._ascii_encode(v1) + '\n')
                                            elif k1 in eval(c):
                                                f.write(' ' * 16 + '"' + k1 + '": ' + self._ascii_encode(v1) + ',\n')
                                        f.write(' ' * 8 + '},\n')
                                    if isinstance(l, list):
                                        # print 'DEBUG: v is list: l is list: %s' % l
                                        f.write(' ' * 8 + '[\n')
                                        for l1 in l:
                                            # print 'DEBUG: v is list: l is list: l1: %s' % l1
                                            f.write(' ' * 8 + self._ascii_encode(l1) + ',\n')
                                        f.write(' ' * 8 + '],\n')
                                f.write(' ' * 4 + '],\n')
                        else:
                            # print 'DEBUG: not in locals: %s' % c
                            f.write(' ' * 4 + '"' + k + '": ' + self._ascii_encode(v) + ',\n')
            f.write('}\n')

    def wpst_generate_ethnets_variable_file(self, ip, sessionId, resourceData, fileName, variableName, vMapFile='../resources/public/ethernet.conf', mode='append'):
        """ Ethernet networks parser for variable file
            [Arguments]
            ip - OV IP
            sessionId - OV session Id
            resourceData - dictionary of resource data
            fileName - file to save parsed data to
            variableName - name of variable to assign parsed data to
            vMapFile - [optional] resource's variable-to-keys mapping
            mode - write or append to fileName
        """

        with open(vMapFile, 'r') as r:
            vConfig = imp.new_module('data')
            exec(r.read(), vConfig.__dict__)
        membersKeys = vConfig.membersKeys

        self.variable_file_generic_parser(ip, sessionId, resourceData, fileName, variableName, membersKeys, mode)

    def wpst_generate_fcnets_variable_file(self, ip, sessionId, resourceData, fileName, variableName, vMapFile='../resources/public/fc.conf', mode='append'):
        """ Fibre Channel Networks parser for variable file
            [Arguments]
            ip - OV IP
            sessionId - OV session Id
            resourceData - dictionary of resource data
            fileName - file to save parsed data to
            variableName - name of variable to assign parsed data to
            vMapFile - [optional] resource's variable-to-keys mapping
            mode - write or append to fileName
        """

        with open(vMapFile, 'r') as r:
            vConfig = imp.new_module('data')
            exec(r.read(), vConfig.__dict__)
        membersKeys = vConfig.membersKeys

        self.variable_file_generic_parser(ip, sessionId, resourceData, fileName, variableName, membersKeys, mode)

    def wpst_generate_fcoenets_variable_file(self, ip, sessionId, resourceData, fileName, variableName, vMapFile='../resources/public/fcoe.conf', mode='append'):
        """ Fibre Channel Networks parser for variable file
            [Arguments]
            ip - OV IP
            sessionId - OV session Id
            resourceData - dictionary of resource data
            fileName - file to save parsed data to
            variableName - name of variable to assign parsed data to
            vMapFile - [optional] resource's variable-to-keys mapping
            mode - write or append to fileName
        """

        with open(vMapFile, 'r') as r:
            vConfig = imp.new_module('data')
            exec(r.read(), vConfig.__dict__)
        membersKeys = vConfig.membersKeys

        self.variable_file_generic_parser(ip, sessionId, resourceData, fileName, variableName, membersKeys, mode)

    def wpst_generate_enclosures_variable_file(self, ip, sessionId, resourceData, fileName, variableName, vMapFile='../resources/public/enclosures.conf', mode='append'):
        """ Enclosures parser for variable file
            [Arguments]
            ip - OV IP
            sessionId - OV session Id
            resourceData - dictionary of resource data
            fileName - file to save parsed data to
            variableName - name of variable to assign parsed data to
            vMapFile - [optional] resource's variable-to-keys mapping
            mode - [optional] write or append to fileName
        """

        with open(vMapFile, 'r') as r:
            vConfig = imp.new_module('data')
            exec(r.read(), vConfig.__dict__)
        membersKeys = vConfig.membersKeys

        self.variable_file_generic_parser(ip, sessionId, resourceData, fileName, variableName, membersKeys, mode)

    def wpst_generate_servers_variable_file(self, ip, sessionId, resourceData, fileName, variableName, vMapFile='../resources/public/servers.conf', mode='append'):
        """ Servers parser for variable file
            [Arguments]
            ip - OV IP
            sessionId - OV session Id
            resourceData - dictionary of resource data
            fileName - file to save parsed data to
            variableName - name of variable to assign parsed data to
            vMapFile - [optional] resource's variable-to-keys mapping
            mode - [optional] write or append to fileName
        """

        with open(vMapFile, 'r') as r:
            vConfig = imp.new_module('data')
            exec(r.read(), vConfig.__dict__)
        membersKeys = vConfig.membersKeys

        self.variable_file_generic_parser(ip, sessionId, resourceData, fileName, variableName, membersKeys, mode)

    def wpst_generate_encgrp_variable_file(self, ip, sessionId, resourceData, fileName, variableName, vMapFile='../resources/public/enclosure-group.conf', mode='append'):
        """ EG parser for variable file
            [Arguments]
            ip - OV IP
            sessionId - OV session Id
            resourceData - dictionary of resource data
            fileName - file to save parsed data to
            variableName - name of variable to assign parsed data to
            vMapFile - [optional] resource's variable-to-keys mapping
            mode - [optional] write or append to fileName
        """

        with open(vMapFile, 'r') as r:
            vConfig = imp.new_module('data')
            exec(r.read(), vConfig.__dict__)
        vKeys = {
            'membersKeys': vConfig.membersKeys,
            'interconnectBayMappingsKeys': vConfig.interconnectBayMappingsKeys,
            'membersDict': vConfig.membersDict,
            'keepUris': vConfig.keepUris,
            'globalNegativeCondDict': vConfig.globalNegativeCondDict,
            'nonglobalNegativeCondDict': vConfig.nonglobalNegativeCondDict
        }

        self.variable_file_generic2_parser(ip, sessionId, resourceData, fileName, variableName, vKeys, mode)

    def wpst_generate_profiles_variable_file(self, ip, sessionId, resourceData, fileName, variableName, vMapFile='../resources/public/profiles.conf', mode='append', CIFIT_TYPE_CONV=False):
        """ profile parser for variable file
            [Arguments]
            ip - OV IP
            sessionId - OV session Id
            resourceData - dictionary of resource data
            fileName - file to save parsed data to
            variableName - name of variable to assign parsed data to
            vMapFile - [optional] resource's variable-to-keys mapping
            mode - [optional] write or append to fileName
        """

        with open(vMapFile, 'r') as r:
            vConfig = imp.new_module('data')
            exec(r.read(), vConfig.__dict__)
        vKeys = {
            'membersKeys': vConfig.membersKeys,
            'connectionsKeys': vConfig.connectionsKeys,
            'membersDict': vConfig.membersDict,
            'keepUris': vConfig.keepUris,
            'globalNegativeCondDict': vConfig.globalNegativeCondDict,
            'nonglobalNegativeCondDict': vConfig.nonglobalNegativeCondDict
        }

        self.variable_file_generic2_parser(ip, sessionId, resourceData, fileName, variableName, vKeys, mode, CIFIT_TYPE_CONV)

    def wpst_generate_networksets_variable_file(self, ip, sessionId, resourceData, fileName, variableName, vMapFile='../resources/public/networksets.conf', mode='append'):
        """ Network Sets parser for variable file
            [Arguments]
            ip - OV IP
            sessionId - OV session Id
            resourceData - dictionary of resource data
            fileName - file to save parsed data to
            variableName - name of variable to assign parsed data to
            vMapFile - [optional] resource's variable-to-keys mapping
            mode - [optional] write or append to fileName
        """

        with open(vMapFile, 'r') as r:
            vConfig = imp.new_module('data')
            exec(r.read(), vConfig.__dict__)
        membersKeys = vConfig.membersKeys

        self.wpst_create_variable_file_header(fileName, mode)
        with open(fileName, 'a') as f:
            f.write(variableName + ' = [\n')
            resourceTools = WPSTConnections()
            for members in resourceData['members']:
                f.write(' ' * 4 + '{\n')
                # get the membersKeys listed above
                for membersKey in membersKeys:
                    if re.search('Uri$', membersKey):
                        # string uri
                        if members[membersKey] is not None:
                            uriName = '"' + resourceTools.get_attr_by_uri(ip, sessionId, members[membersKey]) + '"'
                        else:
                            uriName = str(None)
                        f.write(' ' * 8 + '"' + membersKey + '": ')
                        f.write(uriName)
                        self._close_data(f, membersKey, membersKeys[-1], 0)
                    elif re.search('Uris$', membersKey):
                        # list of uris will be replaced with the networkUri->name
                        f.write(' ' * 8 + '"' + membersKey + '": [\n')
                        for rawUri in members[membersKey]:
                            self._close_data(f, rawUri, members[membersKey][-1], 12, lineEnder='"' + resourceTools.get_attr_by_uri(ip, sessionId, rawUri) + '"')
                        self._close_data(f, membersKey, membersKeys[-1], 8, lineEnder=']')
                    else:
                        members[membersKey] = self._ascii_encode(members[membersKey])
                        f.write(' ' * 8 + '"' + membersKey + '": ' + str(members[membersKey]))
                        self._close_data(f, membersKey, membersKeys[-1], 0)
                self._close_data(f, members, resourceData['members'][-1], 4, lineEnder='}')
            f.write(']\n')

    def wpst_generate_lig_variable_file(self, ip, sessionId, resourceData, fileName, variableName, vMapFile='../resources/public/lig-payload.conf', mode='append'):
        """ Lig parser for variable file
            [Arguments]
            ip - OV IP
            sessionId - OV session Id
            resourceData - dictionary of resource data
            fileName - file to save parsed data to
            variableName - name of variable to assign parsed data to
            vMapFile - [optional] Resource variable-to-keys mapping
            mode - [optional] write or append to fileName
        """

        with open(vMapFile, 'r') as r:
            vConfig = imp.new_module('data')
            exec(r.read(), vConfig.__dict__)
        membersKeys = vConfig.membersKeys
        qosConfigurationKeys = vConfig.qosConfigurationKeys
        activeQosConfigKeys = vConfig.activeQosConfigKeys
        inactiveFCoEQosConfigKeys = vConfig.inactiveFCoEQosConfigKeys
        inactiveNonFCoEQosConfigKeys = vConfig.inactiveNonFCoEQosConfigKeys
        qosTrafficClassifiersKeys = vConfig.qosTrafficClassifiersKeys
        qosClassificationMapping = vConfig.qosClassificationMappingKeys
        qosTrafficClassKeys = vConfig.qosTrafficClassKeys
        ethernetSettingsKeys = vConfig.ethernetSettingsKeys
        interconnectMapTemplateKeys = vConfig.interconnectMapTemplateKeys
        interconnectMapEntryTemplatesKeys = vConfig.interconnectMapEntryTemplatesKeys
        telemetryConfigurationKeys = vConfig.telemetryConfigurationKeys
        snmpConfigurationKeys = vConfig.snmpConfigurationKeys
        uplinkSetsKeys = vConfig.uplinkSetsKeys
        logicalPortConfigInfosKeys = vConfig.logicalPortConfigInfosKeys
        logicalLocationDict = vConfig.logicalLocationDict
        primaryPortDict = vConfig.primaryPortDict
        membersDict = vConfig.membersDict
        dataTypeToSym = vConfig.dataTypeToSym
        customDict = vConfig.customDict
        icmPorts = {}
        bayNumber = 0

        self.wpst_create_variable_file_header(fileName, mode)
        with open(fileName, 'a') as f:
            f.write(variableName + ' = [\n')
            resourceTools = WPSTConnections()
            ligInstance = WPSTLogicalInterconnectGroup()
            for members in resourceData['members']:
                f.write(' ' * 4 + '{\n')
                for membersKey in membersKeys:
                    if membersKey in membersDict:
                        # membersKey is listed in membersDict
                        # build the dict/list
                        f.write(' ' * 8 + '"' + membersKey + '": ' + dataTypeToSym[membersDict[membersKey + '_type'] + '_begin'] + '\n')
                        if membersDict[membersKey + '_type'] == 'listOfDict':
                            # use membersKey in getting the values listed in membersDict[membersKey] list of dictionaries
                            for listOfDictValue in members[membersKey]:
                                f.write(' ' * 8 + '{\n')
                                # get the listed key from each index of list of dictionaries
                                for membersDictKey in membersDict[membersKey]:
                                    if re.search('Uri$', membersDictKey):
                                        # string uri
                                        uriName = None
                                        if listOfDictValue[membersDictKey] is not None:
                                            uriName = resourceTools.get_attr_by_uri(ip, sessionId, listOfDictValue[membersDictKey])
                                        uriName = self._ascii_encode(uriName)
                                        f.write(' ' * 12 + '"' + membersDictKey + '": ' + str(uriName))

                                        self._close_data(f, membersDictKey, members[membersKey][-1], 0)
                                        continue
                                    elif re.search('Uris$', membersDictKey):
                                        # list of uris
                                        f.write(' ' * 12 + '"' + membersDictKey + '": [\n')
                                        for rawUri in listOfDictValue[membersDictKey]:
                                            # TODO: Came across a config with some URI lookup returned error/None/null. I need to figure what data the library
                                            # expect when this happen. For now, leaving it 'empty'/"" so the library won't process it
                                            uriName = resourceTools.get_attr_by_uri(ip, sessionId, rawUri)
                                            uriName = self._ascii_encode(uriName)
                                            if uriName is None:
                                                uriName = ""
                                            f.write(' ' * 16 + str(uriName))
                                            self._close_data(f, rawUri, listOfDictValue[membersDictKey][-1], 0)
                                        f.write(' ' * 12 + '],\n')
                                        continue

                                    # checking for level2 list of dict
                                    if membersDict.get(membersDictKey + '_type') == 'listOfDict':
                                        # create/write the list
                                        if listOfDictValue[membersDictKey] is None:
                                            f.write(' ' * 12 + '"' + membersDictKey + '": None\n')
                                            continue
                                        else:
                                            f.write(' ' * 12 + '"' + membersDictKey + '": [\n')

                                        for level2Value in listOfDictValue[membersDictKey]:
                                            # compose dictionary
                                            f.write(' ' * 16 + '{\n')
                                            tmpList = []
                                            # loop thru list of dict
                                            for level2Key in membersDict[membersDictKey]:
                                                # check with membersDict if something was defined
                                                if level2Key in membersDict:
                                                    # another dictionary processing here (likes of logicalPortConfigInfos values)
                                                    if membersDict[level2Key + '_type'] == 'listOfDict':
                                                        # loop thru logicalLocation key value (dict)
                                                        for level3Value in level2Value[level2Key]:
                                                            # loop thru level3Value (dictionary value)
                                                            for level3Key in membersDict[level2Key]:
                                                                if isinstance(membersDict[level2Key][level3Key], list):
                                                                    # list of dictionaries processing here
                                                                    tmpDict = {}
                                                                    # loop thru the likes of logicalPortConfigInfos->logicalLocation->locationEntries list values
                                                                    for level4Value in level2Value[level2Key][level3Value]:
                                                                        # loop thru each defined keys off membersDict[level2Key][level3Key] list, get the values, and write to file
                                                                        for level5Key in membersDict[level2Key][level3Key]:
                                                                            # added to conform with the existing 2.0 variable type format supported by library
                                                                            customKey = customDict.get(level5Key)
                                                                            if customKey is 'key':
                                                                                myCustomKey = str(level4Value[level5Key]).lower()
                                                                            elif customKey is 'value':
                                                                                myCustomValue = str(level4Value[level5Key])

                                                                        tmpDict[myCustomKey] = myCustomValue
                                                                    # process tmpDict and build key-value pair that conform with 2.0 library/format
                                                                    for tkey, tvalue in tmpDict.iteritems():
                                                                        if customDict.get(tkey) is 'translate':
                                                                            # this is bay (bayNumber)
                                                                            for xkey, xvalue in ligInstance.lig.xport[icmPorts[tvalue]].iteritems():
                                                                                if xvalue == tmpDict['port']:
                                                                                    tmpDict['port'] = xkey
                                                                    for i, (tkey, tvalue) in self.wpst_annotate(tmpDict.iteritems()):
                                                                        strToAppend = '"' + tkey + '": "' + tvalue + '"'
                                                                        if i == '-1':
                                                                            tmpList.append(strToAppend + '\n')
                                                                        else:
                                                                            tmpList.append(strToAppend + ',\n')
                                                else:
                                                    # immediate key-value pair here (no complicated data types)
                                                    if level2Key in customDict:
                                                        modLevel2Key = customDict[level2Key]
                                                    else:
                                                        modLevel2Key = level2Key

                                                    level2Value[level2Key] = self._ascii_encode(level2Value[level2Key])
                                                    f.write(' ' * 20 + '"' + modLevel2Key + '": ' + level2Value[level2Key])
                                                    self._close_data(f, level2Key, listOfDictValue[membersDictKey][-1], 0)
                                            # write the list here (this is to conform with exiting 2.0 variable file formatting)
                                            [f.write(' ' * 20 + k) for k in tmpList if k]
                                            self._close_data(f, level2Value, listOfDictValue[membersDictKey][-1], 16, lineEnder='}')
                                        # end list
                                        self._close_data(f, membersDictKey, members[membersKey][-1], 12, lineEnder=']')
                                    elif membersDict.get(membersDictKey + '_type') == 'modListOfDict':
                                        # create/write the list
                                        if listOfDictValue[membersDictKey] is None:
                                            f.write(' ' * 12 + '"' + membersDictKey + '": None\n')
                                            continue
                                        else:
                                            # compose dictionary
                                            f.write(' ' * 12 + '"' + membersDictKey + '": {\n')
                                            tmpList = []
                                            # get the keys of the dict (primaryPortDict)
                                            for level2Key in membersDict[membersDictKey].keys():
                                                if isinstance(membersDict[membersDictKey][level2Key], list):
                                                    # list of dictionaries processing here
                                                    tmpDict = {}
                                                    # loop thru the likes of primaryPort->locationEntries list values from JSON
                                                    for level2Value in listOfDictValue[membersDictKey][level2Key]:
                                                        # loop thru each defined keys off membersDict[level2Key][level3Key] list, get the values, and write to file
                                                        for level3Key in membersDict[membersDictKey][level2Key]:
                                                            # added to conform with the existing 2.0 variable type format supported by library
                                                            customKey = customDict.get(level3Key)
                                                            if customKey is 'key':
                                                                myCustomKey = str(level2Value[level3Key]).lower()
                                                            elif customKey is 'value':
                                                                myCustomValue = str(level2Value[level3Key])

                                                        tmpDict[myCustomKey] = myCustomValue
                                                    # process tmpDict and build key-value pair that conform with 2.0 library/format
                                                    for tkey, tvalue in tmpDict.iteritems():
                                                        if customDict.get(tkey) is 'translate':
                                                            # this is bay (bayNumber)
                                                            for xkey, xvalue in ligInstance.lig.xport[icmPorts[tvalue]].iteritems():
                                                                if xvalue == tmpDict['port']:
                                                                    tmpDict['port'] = xkey
                                                    for i, (tkey, tvalue) in self.wpst_annotate(tmpDict.iteritems()):
                                                        strToAppend = '"' + tkey + '": "' + tvalue + '"'
                                                        if i == '-1':
                                                            tmpList.append(strToAppend + '\n')
                                                        else:
                                                            tmpList.append(strToAppend + ',\n')
                                            # write the list here (this is to conform with exiting 2.0 variable file formatting)
                                            [f.write(' ' * 16 + k) for k in tmpList if k]
                                            # end list
                                            self._close_data(f, membersDictKey, members[membersKey][-1], 12, lineEnder='}')
                                    else:
                                        # immediate second-level stuff
                                        listOfDictValue[membersDictKey] = self._ascii_encode(listOfDictValue[membersDictKey])
                                        f.write(' ' * 12 + '"' + membersDictKey + '": ')
                                        f.write(str(listOfDictValue[membersDictKey]))
                                        self._close_data(f, membersDictKey, members[membersKey][-1], 0)
                                self._close_data(f, listOfDictValue, members[membersKey][-1], 8, lineEnder='}')
                        elif membersDict[membersKey + '_type'] == 'modDictListOfDict':
                            # get the listed key from each index of list of dictionaries
                            for membersDictKey in membersDict[membersKey]:
                                # checking for level2 list of dict
                                if membersDict.get(membersDictKey + '_type') == 'listOfDict':
                                    # create/write the list
                                    if members[membersKey][membersDictKey] is None:
                                        continue
                                    beginFlag = 1
                                    for level2Value in members[membersKey][membersDictKey]:
                                        # compose dictionary
                                        if beginFlag == 1:
                                            f.write(' ' * 12 + '{\n')
                                        tmpList = []
                                        # loop thru list of dict
                                        for level2Key in membersDict[membersDictKey]:
                                            # this is where the likes of permittedInterconnectTypeUri will be processed
                                            if re.search('Uri$', level2Key):
                                                # string uri
                                                uriName = str(None)
                                                if level2Value[level2Key] is not None:
                                                    uriName = resourceTools.get_attr_by_uri(ip, sessionId, level2Value[level2Key])
                                                if level2Key in customDict:
                                                    tmpList.append('"' + customDict[level2Key] + '": "' + uriName + '"\n')
                                                    icmPorts[str(bayNumber)] = uriName
                                            # check with membersDict if something was defined
                                            elif level2Key in membersDict:
                                                # another dictionary processing here (the likes of interconnectMapEntryTemplates->logicalLocation->locationEntries)
                                                if membersDict[level2Key + '_type'] == 'listOfDict':
                                                    # loop thru logicalLocation key value (dict)
                                                    for level3Value in level2Value[level2Key]:
                                                        # loop thru level3Value (dictionary value)
                                                        for level3Key in membersDict[level2Key]:
                                                            if isinstance(membersDict[level2Key][level3Key], list):
                                                                # it's list of dictionaries
                                                                # loop thru the likes of locationEntries list values
                                                                for level4Value in level2Value[level2Key][level3Value]:
                                                                    # loop thru each defined keys off membersDict[level2Key][level3Key] list, get the values, and write to file
                                                                    for level5Key in membersDict[level2Key][level3Key]:
                                                                        # added to conform with the existing 2.0 variable type format supported by library
                                                                        customKey = customDict.get(level5Key)
                                                                        if customKey is 'key':
                                                                            myCustomKey = level4Value[level5Key]
                                                                        elif customKey is 'value':
                                                                            myCustomValue = level4Value[level5Key]

                                                                    myCustomKey = str(myCustomKey).lower()
                                                                    if myCustomKey == 'bay':
                                                                        # dictionary of icmPorts
                                                                        bayNumber = myCustomValue
                                                                        icmPorts[str(bayNumber)] = None
                                                                    myCustomValue = self._ascii_encode(myCustomValue)
                                                                    tmpList.append('"' + str(myCustomKey) + '": ' + str(myCustomValue) + ',\n')
                                            else:
                                                # immediate key-value pair here (no complicated data types)
                                                level2Value[level2Key] = self._ascii_encode(level2Value[level2Key])
                                                if level2Value[level2Key] is not None:
                                                    f.write(' ' * 16 + '"' + level2Key + '": ' + str(level2Value[level2Key]))
                                                else:
                                                    f.write(' ' * 16 + '"' + level2Key + '": ')
                                                    f.write(str(level2Value[level2Key]))
                                                f.write(',\n')
                                        # write the list here (this is to conform with exiting 2.0 variable file formatting)
                                        if any('"type": "None"\n' == k for k in tmpList if k):
                                            beginFlag = 0
                                            continue
                                        else:
                                            beginFlag = 1
                                        [f.write(' ' * 16 + k) for k in tmpList if k]
                                        self._close_data(f, level2Value, members[membersKey][membersDictKey][-1], 12, lineEnder='}')
                                    # end list
                                else:
                                    # immediate second-level stuff
                                    members[membersKey][membersDictKey] = self._ascii_encode(members[membersKey][membersDictKey])
                                    f.write(' ' * 12 + '"' + membersDictKey + '": ')
                                    f.write(str(members[membersKey][membersDictKey]))
                                self._close_data(f, membersDictKey, membersDict[membersKey][-1], 0)
                        elif membersDict[membersKey + '_type'] == 'dictOfDict':
                            for membersDictKey in membersDict[membersKey]:
                                if membersDict.get(membersDictKey) is not None and members[membersKey][membersDictKey] is not None:
                                    # defined in membersDict
                                    f.write(' ' * 12 + '"' + membersDictKey + '": ' + dataTypeToSym[membersDict[membersDictKey + '_type'] + '_begin'] + '\n')
                                    for level3Key in membersDict.get(membersDictKey):
                                        # the likes of activeQosConfig keys
                                        if membersDict.get(level3Key) is not None:
                                            if membersDict[level3Key + '_type'] == 'listOfDict':
                                                f.write(' ' * 16 + '"' + level3Key + '": ' + dataTypeToSym[membersDict[level3Key + '_type'] + '_begin'] + '\n')
                                                # loop thru the likes of qosTrafficClassifiers list of dict here
                                                for level3Value in members[membersKey][membersDictKey][level3Key]:
                                                    # loop thru every element of the likes of qosTrafficClassifiers
                                                    # for level4Key in membersDict[level3Key]:
                                                    # parsing the likes of qosClassificationMapping
                                                    f.write(' ' * 20)
                                                    f.write(str(level3Value))
                                                    self._close_data(f, level3Value, members[membersKey][membersDictKey][level3Key][-1], 0)
                                                f.write(' ' * 16 + dataTypeToSym[membersDict[level3Key + '_type'] + '_end'])
                                        else:
                                            members[membersKey][membersDictKey][level3Key] = self._ascii_encode(members[membersKey][membersDictKey][level3Key])
                                            f.write(' ' * 16 + '"' + level3Key + '": ')
                                            f.write(str(members[membersKey][membersDictKey][level3Key]))
                                        self._close_data(f, level3Key, membersDict.get(membersDictKey)[-1], 0)
                                    f.write(' ' * 12 + dataTypeToSym[membersDict[membersDictKey + '_type'] + '_end'])
                                else:
                                    # regular key-value pair not in membersDict
                                    members[membersKey][membersDictKey] = self._ascii_encode(members[membersKey][membersDictKey])
                                    f.write(' ' * 12 + '"' + membersDictKey + '": ')
                                    f.write(str(members[membersKey][membersDictKey]))
                                self._close_data(f, membersDictKey, membersDict[membersKey][-1], 0)
                        else:
                            # anything else outside type listOfDict
                            for membersDictKey in membersDict[membersKey]:
                                # grab whatever listed membersDict[membersKey]
                                members[membersKey][membersDictKey] = self._ascii_encode(members[membersKey][membersDictKey])
                                f.write(' ' * 12 + '"' + membersDictKey + '": ')
                                f.write(str(members[membersKey][membersDictKey]))
                                self._close_data(f, membersDictKey, membersDict[membersKey][-1], 0)
                        f.write(' ' * 8 + dataTypeToSym[membersDict[membersKey + '_type'] + '_end'])
                    else:
                        # membersKey has immediate value (not a list or dict key of something else)
                        members[membersKey] = self._ascii_encode(members[membersKey])
                        f.write(' ' * 8 + '"' + membersKey + '": ')
                        f.write(str(members[membersKey]))
                    self._close_data(f, membersKey, membersKeys[-1], 0)
                self._close_data(f, members, resourceData['members'][-1], 4, lineEnder='}')
            f.write(']\n')

    def wpst_generate_lig_variable_file_as_is(self, ip, sessionId, resourceData, fileName, variableName, vMapFile='../resources/public/lig.conf', mode='append'):
        """ Lig parser for variable file
            [Arguments]
            ip - OV IP
            sessionId - OV session Id
            resourceData - dictionary of resource data
            fileName - file to save parsed data to
            variableName - name of variable to assign parsed data to
            vMapFile - [optional] Resource variable-to-keys mapping
            mode - [optional] write or append to fileName
        """

        with open(vMapFile, 'r') as r:
            vConfig = imp.new_module('data')
            exec(r.read(), vConfig.__dict__)
        membersKeys = vConfig.membersKeys
        qosConfigurationKeys = vConfig.qosConfigurationKeys
        activeQosConfigKeys = vConfig.activeQosConfigKeys
        inactiveFCoEQosConfigKeys = vConfig.inactiveFCoEQosConfigKeys
        inactiveNonFCoEQosConfigKeys = vConfig.inactiveNonFCoEQosConfigKeys
        qosTrafficClassifiersKeys = vConfig.qosTrafficClassifiersKeys
        qosClassificationMapping = vConfig.qosClassificationMappingKeys
        qosTrafficClassKeys = vConfig.qosTrafficClassKeys
        ethernetSettingsKeys = vConfig.ethernetSettingsKeys
        interconnectMapTemplateKeys = vConfig.interconnectMapTemplateKeys
        interconnectMapEntryTemplatesKeys = vConfig.interconnectMapEntryTemplatesKeys
        telemetryConfigurationKeys = vConfig.telemetryConfigurationKeys
        snmpConfigurationKeys = vConfig.snmpConfigurationKeys
        uplinkSetsKeys = vConfig.uplinkSetsKeys
        logicalPortConfigInfosKeys = vConfig.logicalPortConfigInfosKeys
        logicalLocationDict = vConfig.logicalLocationDict
        primaryPortDict = vConfig.primaryPortDict
        membersDict = vConfig.membersDict
        dataTypeToSym = vConfig.dataTypeToSym
        customDict = vConfig.customDict
        icmPorts = {}
        bayNumber = 0

        self.wpst_create_variable_file_header(fileName, mode)
        with open(fileName, 'a') as f:
            f.write(variableName + ' = [\n')
            resourceTools = WPSTConnections()
            ligInstance = WPSTLogicalInterconnectGroup()
            for members in resourceData['members']:
                f.write(' ' * 4 + '{\n')
                for membersKey in membersKeys:
                    if membersKey in membersDict:
                        # membersKey is listed in membersDict
                        # build the dict/list
                        f.write(' ' * 8 + '"' + membersKey + '": ' + dataTypeToSym[membersDict[membersKey + '_type'] + '_begin'] + '\n')
                        if membersDict[membersKey + '_type'] == 'listOfDict':
                            # use membersKey in getting the values listed in membersDict[membersKey] list of dictionaries
                            for listOfDictValue in members[membersKey]:
                                f.write(' ' * 8 + '{\n')
                                # get the listed key from each index of list of dictionaries
                                for membersDictKey in membersDict[membersKey]:
                                    # checking for level2 list of dict
                                    if membersDict.get(membersDictKey + '_type') == 'listOfDict':
                                        # create/write the list
                                        if listOfDictValue[membersDictKey] is None:
                                            f.write(' ' * 12 + '"' + membersDictKey + '": None\n')
                                            continue
                                        else:
                                            f.write(' ' * 12 + '"' + membersDictKey + '": [\n')

                                        for level2Value in listOfDictValue[membersDictKey]:
                                            # compose dictionary
                                            f.write(' ' * 16 + '{\n')
                                            tmpList = []
                                            # loop thru list of dict
                                            for level2Key in membersDict[membersDictKey]:
                                                # check with membersDict if something was defined
                                                if level2Key in membersDict:
                                                    # another dictionary processing here (likes of logicalPortConfigInfos values)
                                                    if membersDict[level2Key + '_type'] == 'listOfDict':
                                                        # loop thru logicalLocation key value (dict)
                                                        for level3Value in level2Value[level2Key]:
                                                            # loop thru level3Value (dictionary value)
                                                            for level3Key in membersDict[level2Key]:
                                                                if isinstance(membersDict[level2Key][level3Key], list):
                                                                    # list of dictionaries processing here
                                                                    tmpDict = {}
                                                                    # loop thru the likes of logicalPortConfigInfos->logicalLocation->locationEntries list values
                                                                    for level4Value in level2Value[level2Key][level3Value]:
                                                                        # loop thru each defined keys off membersDict[level2Key][level3Key] list, get the values, and write to file
                                                                        for level5Key in membersDict[level2Key][level3Key]:
                                                                            # added to conform with the existing 2.0 variable type format supported by library
                                                                            customKey = customDict.get(level5Key)
                                                                            if customKey is 'key':
                                                                                myCustomKey = str(level4Value[level5Key]).lower()
                                                                            elif customKey is 'value':
                                                                                myCustomValue = str(level4Value[level5Key])

                                                                        tmpDict[myCustomKey] = myCustomValue
                                                                    # process tmpDict and build key-value pair that conform with 2.0 library/format
                                                                    for tkey, tvalue in tmpDict.iteritems():
                                                                        if customDict.get(tkey) is 'translate':
                                                                            # this is bay (bayNumber)
                                                                            for xkey, xvalue in ligInstance.lig.xport[icmPorts[tvalue]].iteritems():
                                                                                if xvalue == tmpDict['port']:
                                                                                    tmpDict['port'] = xkey
                                                                    for i, (tkey, tvalue) in self.wpst_annotate(tmpDict.iteritems()):
                                                                        strToAppend = '"' + tkey + '": "' + tvalue + '"'
                                                                        if i == '-1':
                                                                            tmpList.append(strToAppend + '\n')
                                                                        else:
                                                                            tmpList.append(strToAppend + ',\n')
                                                else:
                                                    # immediate key-value pair here (no complicated data types)
                                                    if level2Key in customDict:
                                                        modLevel2Key = customDict[level2Key]
                                                    else:
                                                        modLevel2Key = level2Key

                                                    level2Value[level2Key] = self._ascii_encode(level2Value[level2Key])
                                                    f.write(' ' * 20 + '"' + modLevel2Key + '": ' + level2Value[level2Key])
                                                    self._close_data(f, level2Key, listOfDictValue[membersDictKey][-1], 0)
                                            # write the list here (this is to conform with exiting 2.0 variable file formatting)
                                            [f.write(' ' * 20 + k) for k in tmpList if k]
                                            self._close_data(f, level2Value, listOfDictValue[membersDictKey][-1], 16, lineEnder='}')
                                        # end list
                                        self._close_data(f, membersDictKey, members[membersKey][-1], 12, lineEnder=']')
                                    elif membersDict.get(membersDictKey + '_type') == 'modListOfDict':
                                        # create/write the list
                                        if listOfDictValue[membersDictKey] is None:
                                            f.write(' ' * 12 + '"' + membersDictKey + '": None\n')
                                            continue
                                        else:
                                            # compose dictionary
                                            f.write(' ' * 12 + '"' + membersDictKey + '": {\n')
                                            tmpList = []
                                            # get the keys of the dict (primaryPortDict)
                                            for level2Key in membersDict[membersDictKey].keys():
                                                if isinstance(membersDict[membersDictKey][level2Key], list):
                                                    # list of dictionaries processing here
                                                    tmpDict = {}
                                                    # loop thru the likes of primaryPort->locationEntries list values from JSON
                                                    for level2Value in listOfDictValue[membersDictKey][level2Key]:
                                                        # loop thru each defined keys off membersDict[level2Key][level3Key] list, get the values, and write to file
                                                        for level3Key in membersDict[membersDictKey][level2Key]:
                                                            # added to conform with the existing 2.0 variable type format supported by library
                                                            customKey = customDict.get(level3Key)
                                                            if customKey is 'key':
                                                                myCustomKey = str(level2Value[level3Key]).lower()
                                                            elif customKey is 'value':
                                                                myCustomValue = str(level2Value[level3Key])

                                                        tmpDict[myCustomKey] = myCustomValue
                                                    # process tmpDict and build key-value pair that conform with 2.0 library/format
                                                    for tkey, tvalue in tmpDict.iteritems():
                                                        if customDict.get(tkey) is 'translate':
                                                            # this is bay (bayNumber)
                                                            for xkey, xvalue in ligInstance.lig.xport[icmPorts[tvalue]].iteritems():
                                                                if xvalue == tmpDict['port']:
                                                                    tmpDict['port'] = xkey
                                                    for i, (tkey, tvalue) in self.wpst_annotate(tmpDict.iteritems()):
                                                        strToAppend = '"' + tkey + '": "' + tvalue + '"'
                                                        if i == '-1':
                                                            tmpList.append(strToAppend + '\n')
                                                        else:
                                                            tmpList.append(strToAppend + ',\n')
                                            # write the list here (this is to conform with exiting 2.0 variable file formatting)
                                            [f.write(' ' * 16 + k) for k in tmpList if k]
                                            # end list
                                            self._close_data(f, membersDictKey, members[membersKey][-1], 12, lineEnder='}')
                                    else:
                                        # immediate second-level stuff
                                        listOfDictValue[membersDictKey] = self._ascii_encode(listOfDictValue[membersDictKey])
                                        f.write(' ' * 12 + '"' + membersDictKey + '": ')
                                        f.write(str(listOfDictValue[membersDictKey]))
                                        self._close_data(f, membersDictKey, members[membersKey][-1], 0)
                                self._close_data(f, listOfDictValue, members[membersKey][-1], 8, lineEnder='}')
                        elif membersDict[membersKey + '_type'] == 'modDictListOfDict':
                            # get the listed key from each index of list of dictionaries
                            for membersDictKey in membersDict[membersKey]:
                                # checking for level2 list of dict
                                if membersDict.get(membersDictKey + '_type') == 'listOfDict':
                                    # create/write the list
                                    if members[membersKey][membersDictKey] is None:
                                        continue
                                    beginFlag = 1
                                    for level2Value in members[membersKey][membersDictKey]:
                                        # compose dictionary
                                        if beginFlag == 1:
                                            f.write(' ' * 12 + '{\n')
                                        tmpList = []
                                        # loop thru list of dict
                                        for level2Key in membersDict[membersDictKey]:
                                            # immediate key-value pair here (no complicated data types)
                                            level2Value[level2Key] = self._ascii_encode(level2Value[level2Key])
                                            if level2Value[level2Key] is not None:
                                                f.write(' ' * 16 + '"' + level2Key + '": ' + str(level2Value[level2Key]))
                                            else:
                                                f.write(' ' * 16 + '"' + level2Key + '": ')
                                                f.write(str(level2Value[level2Key]))
                                            f.write(',\n')
                                        # write the list here (this is to conform with exiting 2.0 variable file formatting)
                                        if any('"type": "None"\n' == k for k in tmpList if k):
                                            beginFlag = 0
                                            continue
                                        else:
                                            beginFlag = 1
                                        [f.write(' ' * 16 + k) for k in tmpList if k]
                                        self._close_data(f, level2Value, members[membersKey][membersDictKey][-1], 12, lineEnder='}')
                                    # end list
                                else:
                                    # immediate second-level stuff
                                    members[membersKey][membersDictKey] = self._ascii_encode(members[membersKey][membersDictKey])
                                    f.write(' ' * 12 + '"' + membersDictKey + '": ')
                                    f.write(str(members[membersKey][membersDictKey]))
                                self._close_data(f, membersDictKey, membersDict[membersKey][-1], 0)
                        elif membersDict[membersKey + '_type'] == 'dictOfDict':
                            for membersDictKey in membersDict[membersKey]:
                                if membersDict.get(membersDictKey) is not None and members.get(membersKey) is not None and members[membersKey].get(membersDictKey) is not None:
                                    # defined in membersDict
                                    f.write(' ' * 12 + '"' + membersDictKey + '": ' + dataTypeToSym[membersDict[membersDictKey + '_type'] + '_begin'] + '\n')
                                    for level3Key in membersDict.get(membersDictKey):
                                        # the likes of activeQosConfig keys
                                        if membersDict.get(level3Key) is not None:
                                            if membersDict[level3Key + '_type'] == 'listOfDict':
                                                f.write(' ' * 16 + '"' + level3Key + '": ' + dataTypeToSym[membersDict[level3Key + '_type'] + '_begin'] + '\n')
                                                # loop thru the likes of qosTrafficClassifiers list of dict here
                                                for level3Value in members[membersKey][membersDictKey][level3Key]:
                                                    # loop thru every element of the likes of qosTrafficClassifiers
                                                    # for level4Key in membersDict[level3Key]:
                                                    # parsing the likes of qosClassificationMapping
                                                    f.write(' ' * 20)
                                                    f.write(str(level3Value))
                                                    self._close_data(f, level3Value, members[membersKey][membersDictKey][level3Key][-1], 0)
                                                f.write(' ' * 16 + dataTypeToSym[membersDict[level3Key + '_type'] + '_end'])
                                        else:
                                            members[membersKey][membersDictKey][level3Key] = self._ascii_encode(members[membersKey][membersDictKey][level3Key])
                                            f.write(' ' * 16 + '"' + level3Key + '": ')
                                            f.write(str(members[membersKey][membersDictKey][level3Key]))
                                        self._close_data(f, level3Key, membersDict.get(membersDictKey)[-1], 0)
                                    f.write(' ' * 12 + dataTypeToSym[membersDict[membersDictKey + '_type'] + '_end'])
                                else:
                                    # regular key-value pair not in membersDict
                                    if members.get(membersKey) is None:
                                        continue
                                    members[membersKey][membersDictKey] = self._ascii_encode(members[membersKey][membersDictKey])
                                    f.write(' ' * 12 + '"' + membersDictKey + '": ')
                                    f.write(str(members[membersKey][membersDictKey]))
                                self._close_data(f, membersDictKey, membersDict[membersKey][-1], 0)
                        else:
                            # anything else outside type listOfDict
                            for membersDictKey in membersDict[membersKey]:
                                # interconnectMapEntryTemplates
                                if membersDict.get(membersDictKey) is not None:
                                    if membersDict[membersDictKey + '_type'] == 'listOfDict':
                                        f.write(' ' * 12 + '"' + membersDictKey + '": ' + dataTypeToSym[membersDict[membersDictKey + '_type'] + '_begin'] + '\n')
                                        for level2Value in members[membersKey][membersDictKey]:
                                            f.write(' ' * 16 + '{\n')
                                            for i, (tkey, tvalue) in self.wpst_annotate(level2Value.iteritems()):
                                                # print 'DEBUG: tkey: %s, tvalue: %s' % (tkey, tvalue)
                                                # print 'DEBUG: membersDict[membersDictKey]: %s' % membersDict[membersDictKey]
                                                if tkey in membersDict[membersDictKey]:
                                                    # print 'DEBUG: tkey has match: %s' % tkey
                                                    f.write(' ' * 20)
                                                    f.write('"' + tkey + '": ')
                                                    tvalue = self._ascii_encode(tvalue)
                                                    f.write(str(tvalue))
                                                    if i == '-1':
                                                        f.write('\n')
                                                    else:
                                                        f.write(',\n')
                                            f.write(' ' * 16 + '}')
                                            self._close_data(f, level2Value, members[membersKey][membersDictKey][-1], 0)
                                        f.write(' ' * 12 + dataTypeToSym[membersDict[membersDictKey + '_type'] + '_end'] + '\n')
                                else:
                                    # grab whatever listed membersDict[membersKey]
                                    if membersDictKey not in members[membersKey]:
                                        continue
                                    members[membersKey][membersDictKey] = self._ascii_encode(members[membersKey][membersDictKey])
                                    f.write(' ' * 12 + '"' + membersDictKey + '": ')
                                    f.write(str(members[membersKey][membersDictKey]))
                                    self._close_data(f, membersDictKey, membersDict[membersKey][-1], 0)
                        f.write(' ' * 8 + dataTypeToSym[membersDict[membersKey + '_type'] + '_end'])
                    else:
                        # membersKey has immediate value (not a list or dict key of something else)
                        if members.get(membersKey) is None:
                            continue
                        members[membersKey] = self._ascii_encode(members[membersKey])
                        f.write(' ' * 8 + '"' + membersKey + '": ')
                        f.write(str(members[membersKey]))
                    self._close_data(f, membersKey, membersKeys[-1], 0)
                self._close_data(f, members, resourceData['members'][-1], 4, lineEnder='}')
            f.write(']\n')

    def wpst_set_variables_in_file(self, fileName, variableNames):
        """ Set the variables to use in the variable file
            [Arguments]
            fileName - Name of variable file
            variableNames - List of variable names to set/use in the file
        """

        with open(fileName, 'a') as f:
            f.write('\ndefault_variables = {\n')
            for variableName in variableNames:
                f.write(' ' * 4 + '"' + variableName + '": ')
                f.write(variableName)
                self._close_data(f, variableName, variableNames[-1], 0)
            f.write('}\n\n\n')
            f.write('def get_variables():\n')
            f.write(' ' * 4 + '""" Auto-generated function for the variable python file """\n\n')
            f.write(' ' * 4 + 'variables = default_variables\n')
            f.write(' ' * 4 + 'return variables\n')

    def create_list_of_uris(self, ip, sessionId, members, membersKey, api=None, headers=None):
        """ Create list of applicable uris off the resourceData based on membersKey
            [Arguments]
            ip - OV IP
            sessionId - OV session Id
            members - resourceData['members'] list of dictionaries
            membersKey - key of a list off resourceData dictionary
            [Return]
            list of Uris
        """

        resourceTools = WPSTConnections()
        responseNameList = []
        for rawUri in members[membersKey]:
            responseName = resourceTools.get_attr_by_uri(ip, sessionId, rawUri, api=api, headers=headers)
            responseNameList.append(responseName)

        return responseNameList

    def wpst_create_variable_file_header(self, fileName, mode):
        """ Open file for write/append
            [Arguments]
            fileName - file name
            mode - write or append. Default is append.
        """

        mode = mode.lower()
        fileMode = {
            'write': 'w',
            'append': 'a'
        }
        fileModeHeader = {
            'write': '#!/usr/bin/env python\n\n',
            'append': '\n'
        }
        if mode not in fileMode:
            print 'Warning: Unsupported file access mode in %s.%s' % (__file__, 'wpst_create_variable_file_header')
        with open(fileName, fileMode[mode]) as f:
            f.write(fileModeHeader[mode])

    def variable_file_generic_parser(self, ip, sessionId, resourceData, fileName, variableName, jsonKeysList, mode='append'):
        """ Generic parser for variable file
            [Arguments]
            ip - OV IP
            sessionId - OV session Id
            resourceData - dictionary of resource data
            fileName - file to save parsed data to
            variableName - name of variable to assign parsed data to
            jsonKeyList - list of keys to be parsed
            mode - write or append to fileName
        """

        self.wpst_create_variable_file_header(fileName, mode)
        resourceTools = WPSTConnections()
        with open(fileName, 'a') as f:
            f.write(variableName + ' = [\n')
            for members in resourceData['members']:
                f.write(' ' * 4 + '{\n')
                for key in jsonKeysList:
                    if re.search('Uri$', key):
                        uriName = str(None)
                        if members[key] is not None:
                            uriName = resourceTools.get_attr_by_uri(ip, sessionId, members[key])
                        f.write(' ' * 8 + '"' + key + '": ')
                        f.write('"' + str(uriName) + '"')
                    else:
                        if key not in members:
                            continue
                        members[key] = self._ascii_encode(members[key])
                        f.write(' ' * 8 + '"' + key + '": ')
                        f.write(str(members[key]))
                    self._close_data(f, key, jsonKeysList[-1], 0)
                self._close_data(f, members, resourceData['members'][-1], 4, lineEnder='}')
            f.write(']\n')

    def variable_file_generic2_parser(self, ip, sessionId, resourceData, fileName, variableName, vKeys, mode, CIFIT_TYPE_CONV=False):
        """ Generic2 parser. Used by profiles, EG
        """

        self.wpst_create_variable_file_header(fileName, mode)
        resourceTools = WPSTConnections()
        with open(fileName, 'a') as f:
            f.write(variableName + ' = [\n')
            for members in resourceData['members']:
                f.write(' ' * 4 + '{\n')
                for membersKey in vKeys['membersKeys']:
                    if membersKey not in vKeys['membersDict']:
                        # not a list of dict
                        if re.search('Uri$', membersKey) and not any(membersKey == x for x in vKeys['keepUris'] if x):
                            uriName = str(None)
                            if members[membersKey] is not None:
                                uriName = resourceTools.get_attr_by_uri(ip, sessionId, members[membersKey])
                            f.write(' ' * 8 + '"' + membersKey + '": ')
                            f.write('"' + str(uriName) + '"')
                        # check for conditional keys (global)
                        elif vKeys['globalNegativeCondDict'].get(membersKey) is not None and vKeys['globalNegativeCondDict'].get(membersKey) != members[membersKey] and vKeys['globalNegativeCondDict'].get(membersKey + '_' + members[membersKey]) is not None:
                            for k in vKeys['globalNegativeCondDict'].get(membersKey + '_' + members[membersKey]):
                                members[k] = self._ascii_encode(members[k])
                                f.write(' ' * 8 + '"' + k + '": ' + str(members[k]) + ',\n')
                            members[membersKey] = self._ascii_encode(members[membersKey])
                            f.write(' ' * 8 + '"' + membersKey + '": ' + str(members[membersKey]))
                        else:
                            if membersKey not in members:
                                continue
                            if CIFIT_TYPE_CONV is True and membersKey == 'serialNumberType' and members[membersKey] == 'Virtual':
                                members[membersKey] = 'UserDefined'
                            members[membersKey] = self._ascii_encode(members[membersKey])
                            f.write(' ' * 8 + '"' + membersKey + '": ' + str(members[membersKey]))
                        self._close_data(f, membersKey, vKeys['membersKeys'][-1], 0)
                    elif vKeys['membersDict'][membersKey + '_type'] == 'listOfDict':
                        # build the list of dictionary
                        f.write(' ' * 8 + '"' + membersKey + '": [\n')
                        # loop thru that members list of dict (like connections list declared above)
                        for membersInDict in members[membersKey]:
                            f.write(' ' * 12 + '{\n')
                            # get the data from the keys listed in the likes of connections(in connectionsKeys)
                            for membersList in vKeys['membersDict'][membersKey]:
                                if re.search('Uri$', membersList) and not any(membersList == x for x in vKeys['keepUris'] if x):
                                    uriName = str(None)
                                    if membersInDict[membersList] is not None:
                                        uriName = resourceTools.get_attr_by_uri(ip, sessionId, membersInDict[membersList])
                                    f.write(' ' * 16 + '"' + membersList + '": ')
                                    f.write('"' + str(uriName) + '"')
                                # check for conditional keys (non-global)
                                elif vKeys['nonglobalNegativeCondDict'].get(membersList) is not None and vKeys['nonglobalNegativeCondDict'].get(membersList) != membersInDict[membersList] and vKeys['nonglobalNegativeCondDict'].get(membersList + '_' + membersInDict[membersList]) is not None:
                                    for k in vKeys['nonglobalNegativeCondDict'].get(membersList + '_' + membersInDict[membersList]):
                                        membersInDict[k] = self._ascii_encode(membersInDict[k])
                                        f.write(' ' * 16 + '"' + k + '": ' + str(membersInDict[k]) + ',\n')
                                    f.write(' ' * 16 + '"' + membersList + '": ')
                                    membersInDict[membersList] = self._ascii_encode(membersInDict[membersList])
                                    f.write(str(membersInDict[membersList]))
                                else:
                                    f.write(' ' * 16 + '"' + membersList + '": ')
                                    if CIFIT_TYPE_CONV is True and membersList == 'macType' and membersInDict[membersList] == 'Virtual':
                                        membersInDict[membersList] = 'UserDefined'
                                    membersInDict[membersList] = self._ascii_encode(membersInDict[membersList])
                                    f.write(str(membersInDict[membersList]))
                                self._close_data(f, membersList, vKeys['membersDict'][membersKey][-1], 0)
                            self._close_data(f, membersInDict, members[membersKey][-1], 12, lineEnder='}')
                        self._close_data(f, membersKey, vKeys['membersKeys'][-1], 8, lineEnder=']')
                self._close_data(f, members, resourceData['members'][-1], 4, lineEnder='}')
            f.write(']\n')

    def wpst_annotate(self, gen):
        prev_key, prev_val = 0, gen.next()
        for k, v in enumerate(gen, start=1):
            yield prev_key, prev_val
            prev_key, prev_val = k, v
        yield '-1', prev_val

    def wpst_deep_copy(self, srcObj):
        """ Robot Framework has a bug particularly in Copy Dictionary.
            It appear to create reference instead of a mutable one.
            Wrapping deep copy to get around this issue.
        """
        destObj = copy.deepcopy(srcObj)

        return destObj

    def wpst_return_nonzero_count(self, dict1, dict2):
        """ Robot Framework appeared to have issue with conditional
        variable assignment operation.
        :param dict1: Dictionary1
        :param dict2: Dictionary2
        :return: Dictionary with none-zero count key value
        """
        if dict1['count'] == 0:
            return dict2
        else:
            return dict1

    def _ascii_encode(self, input):
        """ Encode string to ascii and return as quoted string.
        :param strIn: Input string
        :return: Ascii encoded and quoted string
        """
        if isinstance(input, (str, unicode)):
            input.encode('ascii', 'xmlcharrefreplace')
            input = '"' + input + '"'
        else:
            input = str(input)

        return input

    def _close_data(self, f, arrayElement, arrayLastElement, spacing, lineEnder=''):
        """ Close data type with appropriate spacing and/or line-ending character(s)
        :param f: open file append object
        :param arrayElement: element of a list
        :param arrayLastElement: last element of a list
        :param spacing: number of spaces to write
        :param lineEnder: optional line-ending character(s)
        """
        if arrayElement is not arrayLastElement:
            f.write(' ' * spacing + lineEnder + ',\n')
        else:
            f.write(' ' * spacing + lineEnder + '\n')

    def wpst_check_dataFiles_dir_exist(self, datafiles_loc):
        """ Function checks the default dataFiles directory"""
        try:
            if os.path.exists(datafiles_loc):
                if os.path.isfile(datafiles_loc):
                    logger.info('A file with the same name as your expected dataFiles directory (%s) was found' % datafiles_loc)
                    logger.info('Please remove the existing file or specify a different dataFiles directory name')
                    errMsg = '[%s] dataFiles directory name/path provided (%s) conflicted with an existing file' % (__file__, datafiles_loc)
                    raise RuntimeError(errMsg)
            else:
                logger.info('Datafiles directory named (%s) does not exist.' % datafiles_loc)
                logger.info('Creating the directory (%s) now...' % datafiles_loc)
                os.makedirs(datafiles_loc)
        except Exception, e:
                logger.info("Datafiles directory check failed")
                raise Exception("Datafiles directory check failed", e)

    def wpst_send_email(self, fromAddr, toAddr, subject, message, attach=None):
        email = EmailClient(fromAddr)
        email.send(message, subject, toAddr, attach)

    def sortList(self, beforeList, index, sortDict=True):
        # sort keys for list of dictionaries
        if isinstance(beforeList[0], dict) and sortDict:
            if index in beforeList[0]:
                return sorted(beforeList, key=lambda k: k[index])
            else:
                return beforeList
        else:
            return sorted(beforeList)
