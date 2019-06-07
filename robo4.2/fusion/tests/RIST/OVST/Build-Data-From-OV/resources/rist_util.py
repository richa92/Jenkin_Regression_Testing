import re
import os
import imp
import copy
import json
from RoboGalaxyLibrary.utilitylib import logging as logger
from FusionLibrary.api.common.request import HttpVerbs
from FusionLibrary.api.servers.connections import Connections
from FusionLibrary.api.networking.logical_interconnect_groups import LogicalInterconnectGroup
import data_variables
import collections
import operator
import unicodedata
import re


class RistResourceTools(object):

    def __init__(self):
        self.fusion_client = HttpVerbs()


class RistConnections(RistResourceTools):

    def __init__(self):
        RistResourceTools.__init__(self)
        self.conn = Connections(self.fusion_client)

    def rist_get_connections(self, sessionId, uri=None, param='', api=None, headers=None):
        """Gets default or paginated collection of Connections
        [Arguments]
        sessionId: aka authentication token
        uri: the uri of the resource to retrieve. if omitted, all are returned
        param: query parameters
        [Example]
        ${resp} = Rist Get Connections | <uri> | <param> | <api> | <headers>
         """

        if api:
            headers = self.fusion_client._set_req_api_version(api=api)
        elif headers is None:
            headers = self.fusion_client._headers
        headers['auth'] = sessionId
        return (self.conn.get(uri=uri, api=api, headers=headers, param=param))

    def get_current_api_version(self, ip, sessionId, rawUri, attr='currentVersion', api=None, headers=None):
        """
        Get API Version of Oneview Build
        """

        rawUri = '/rest/version'
        uri = '%s%s' % (ip, rawUri)
        if api:
            headers = self.fusion_client._set_req_api_version(api=api)
        elif headers is None:
            headers = self.fusion_client._headers
        headers['auth'] = sessionId
        response = self.conn.get(uri=uri, headers=headers)
        return response.get(attr)

    def get_storage_pools(self, ip, sessionId, rawUri='/rest/storage-pools', api=None, headers=None):
        """
        Get Storage pool URI by Name
        """
        uri = '%s%s' % (ip, rawUri)
        if api:
            headers = self.fusion_client._set_req_api_version(api=api)
        elif headers is None:
            headers = self.fusion_client._headers
        headers['auth'] = sessionId
        response = self.conn.get(uri=uri, headers=headers)
        return response

    def get_interconnect_bay(self, ip, sessionId, rawUri, api=None, headers=None):
        """
        Get Bay number of Potash Interconnect Model
        """
        uri = '%s%s' % (ip, rawUri)
        baynumber = None
        if api:
            headers = self.fusion_client._set_req_api_version(api=api)
        elif headers is None:
            headers = self.fusion_client._headers
        headers['auth'] = sessionId
        response = self.conn.get(uri=uri, headers=headers)
        for cont in response['interconnectBays']:
            if cont['interconnectModel'] == 'Virtual Connect SE 40Gb F8 Module for Synergy':
                print "Potash Module is found"
                baynumber = cont['bayNumber']
                break
        return baynumber

    def get_ipv4_ranges(self, ip, sessionId, rawUri, api=None, headers=None):
        """
        Get IPV4 ranges and ranges of pooltype MAC, WWN and VSN
        """
        uri = '%s%s' % (ip, rawUri)
        if api:
            headers = self.fusion_client._set_req_api_version(api=api)
        elif headers is None:
            headers = self.fusion_client._headers
        headers['auth'] = sessionId
        response = self.conn.get(uri=uri, headers=headers)
        return response

    def get_attr_by_uri(self, ip, sessionId, rawUri, attr='name', api=None, headers=None):
        """ Get attribute off the Uri
            [Arguments]
            rawUri - raw resource Uri
            attr - attribute default to 'name'
            [Return]
            value of key name
        """

        uri = '%s%s' % (ip, rawUri)
        if "subnets" in uri:
            attr = 'networkId'
        if api:
            headers = self.fusion_client._set_req_api_version(api=api)
        elif headers is None:
            headers = self.fusion_client._headers
        headers['auth'] = sessionId
        response = self.conn.get(uri=uri, headers=headers)
        print "RESPONSE::::", response
        print "uri of path", api, response.get(attr)
        return response.get(attr)

    def add_tagname_to_uri(self, ip, sessionId, uri, api=None):
        """ Add tag to uri based on uri type """
        taggs = {'enclosure-groups': 'EG', 'sas-logical-interconnect-groups': 'SASLIG',
                 'logical-interconnect-groups': 'LIG', 'server-hardware-types': 'SHT',
                 'server-hardware': 'SH', 'enclosures': 'ENC', 'ethernet-networks': 'ETH',
                 'fc-networks': 'FC', 'fcoe-networks': 'FCOE', 'server-profile-templates': 'SPT',
                 'storage-volumes': 'SVOL', 'storage-volume-templates': 'SVT',
                 'server-profiles': 'SP', 'fc-sans': 'SAN', 'network-sets': 'NS',
                 'storage-systems': 'SSYS', 'storage-pools': 'SPOOL', 'logical-enclosures': 'LE'}

        uri_type = uri.split('/')[2]
        if uri_type == "users":
            uri_name_with_out_tagg = self.get_attr_by_uri(ip, sessionId, uri, attr='uri', api=api)
        elif uri_type == "storage-pools":
            uri_name_with_out_tagg = self.get_attr_by_uri(ip, sessionId, uri, attr='storageSystemUri', api=api)
        else:
            uri_name_with_out_tagg = self.get_attr_by_uri(ip, sessionId, uri, api=api)
        if uri_type in taggs:
            tagg = taggs[uri_type]
        else:
            tagg = None
        if tagg:
            uri_name = tagg + ':' + uri_name_with_out_tagg
        else:
            uri_name = uri_name_with_out_tagg
        return uri_name

    def get_mezz_model_by_shtname(self, ip, sessionId, uri, api=None):
        uri = '%s%s' % (ip, uri)
        if api:
            headers = self.fusion_client._set_req_api_version(api=api)
        elif headers is None:
            headers = self.fusion_client._headers
        headers['auth'] = sessionId
        response = self.conn.get(uri=uri, headers=headers)
        templist = response['adapters']
        adapterlist = sorted(templist, key=operator.itemgetter('slot'))
        name = ''
        for adapt in adapterlist:
            if 'location' in adapt:
                if adapt['location'] == 'Flb' or adapt['location'] == 'Lom':
                    name += str(adapt['location']) + str(adapt['slot']) + ':' + adapt['model'] + ':'
                else:
                    name += str(adapt['slot']) + ':' + adapt['model'] + ':'
        shtname = 'SHT:' + response['name'] + ':' + name
        return shtname.rstrip(':')


class RistLogicalInterconnectGroup(RistResourceTools):

    def __init__(self):
        RistResourceTools.__init__(self)
        self.lig = LogicalInterconnectGroup(self.fusion_client)


class rist_util(object):
    def rist_generate_timeandlocale_variable_file(self, ip, sessionId, resourceData, fileName, variableName, vMapFile='../resources/config-files/time-locale.conf', mode='append', apiVersion=None):
        """ Appliance Time and Locale  parser for variable file
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
        self.rist_create_variable_file_header(fileName, mode)
        resourceTools = RistConnections()
        answerlist = {}
        for key, value in resourceData.items():
            for membersKey in membersKeys:
                if membersKey not in key:
                    continue
                if isinstance(key, unicode):
                    key = unicodedata.normalize('NFKD', key).encode('ascii', 'ignore')
                if isinstance(value, unicode):
                    value = unicodedata.normalize('NFKD', value).encode('ascii', 'ignore')
                answerlist[key] = value
        with open(fileName, 'a') as f:
            f.write(variableName + '= ')
            f.write(str(answerlist))
            f.close()

    def rist_generate_appnetworks_variable_file(self, ip, sessionId, resourceData, fileName, variableName, vMapFile='../resources/config-files/appliance-networks.conf', mode='append', apiVersion=None):
        """ Appliance Networks parser for variable file
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
        self.rist_create_variable_file_header(fileName, mode)
        resourceTools = RistConnections()
        with open(fileName, 'a') as f:
            f.write(variableName + '= {\n')
            f.write("'type'" + ': "' + resourceData['type'] + '",\n')
            f.write("'applianceNetworks' : \n")
            for members in resourceData['applianceNetworks']:
                f.write(' ' * 4 + '[{\n')
                for membersKey in membersKeys:
                    if membersKey not in members:
                        continue
                    members[membersKey] = self._ascii_encode(members[membersKey])
                    f.write(' ' * 8 + '"' + membersKey + '": ')
                    f.write(str(members[membersKey]))
                    self._close_data(f, membersKey, membersKeys[-1], 0)
                self._close_data(f, members, resourceData['applianceNetworks'][-1], 4, lineEnder='}')
            f.write(']}\n')
            f.close()

    def rist_generate_licenses_variable_file(self, ip, sessionId, resourceData, fileName, variableName, vMapFile='../resources/config-files/licenses.conf', mode='append', apiVersion=None):
        """ Licenses parser for variable file
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
        self.rist_create_variable_file_header(fileName, mode)
        resourceTools = RistConnections()
        with open(fileName, 'a') as f:
            f.write(variableName + '= [\n')
            for members in resourceData['members']:
                f.write(' ' * 4 + '{\n')
                for membersKey in membersKeys:
                    if membersKey not in members:
                        continue
                    f.write(' ' * 8 + "'" + membersKey + "': ")
                    f.write("'" + members[membersKey] + "'")
                    self._close_data(f, membersKey, membersKeys[-1], 0)
                self._close_data(f, members, resourceData['members'][-1], 4, lineEnder='}')
            f.write(']\n')
            f.close()

    def rist_generate_ipv4_subnet_variable_file(self, ip, sessionId, resourceData, fileName, variableName, vMapFile='../resources/config-files/ipv4_subnet.conf', mode='append', apiVersion=None):
        """ IPV4 Subnet parser for variable file
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
        self.rist_create_variable_file_header(fileName, mode)
        resourceTools = RistConnections()
        with open(fileName, 'a') as f:
            f.write(variableName + '= [\n')
            for members in resourceData['members']:
                f.write(' ' * 4 + '{\n')
                for membersKey in membersKeys:
                    if membersKey == 'name':
                        pair = {membersKey: members['networkId']}
                        members.update(pair)
                    if membersKey not in members:
                        continue
                    members[membersKey] = self._ascii_encode(members[membersKey])
                    if str(members[membersKey]) == '[]':
                        members[membersKey] = str(None)
                    f.write(' ' * 8 + "'" + membersKey + "': ")
                    f.write(str(members[membersKey]))
                    self._close_data(f, membersKey, membersKeys[-1], 0)
                self._close_data(f, members, resourceData['members'][-1], 4, lineEnder='}')
            f.write(']\n')
            f.close()

    def rist_generate_ipv4_ranges_variable_file(self, ip, sessionId, resourceData, fileName, variableName, vMapFile='../resources/config-files/ipv4_ranges.conf', mode='append', apiVersion=None):
        """ IPV4 Ranges for variable file
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
        self.rist_create_variable_file_header(fileName, mode)
        resourceTools = RistConnections()
        rangedata = []
        with open(fileName, 'a') as f:
            f.write(variableName + '= [\n')
            for members in resourceData['rangeUris']:
                ipv4_data = resourceTools.get_ipv4_ranges(ip, sessionId, members, api=apiVersion)
                rangedata.append(ipv4_data)
            for member in rangedata:
                f.write(' ' * 4 + '{\n')
                for membersKey in membersKeys:
                    if membersKey not in member:
                        continue
                    if re.search('Uri$', membersKey):
                        uriName = str(None)
                        if member[membersKey] is not None:
                            uriName = resourceTools.get_attr_by_uri(ip, sessionId, member[membersKey], api=apiVersion)
                        f.write(' ' * 8 + '"' + membersKey + '": ')
                        f.write('"' + str(uriName) + '"')
                    else:
                        member[membersKey] = self._ascii_encode(member[membersKey])
                        f.write(' ' * 8 + "'" + membersKey + "': ")
                        f.write(str(member[membersKey]))
                    self._close_data(f, membersKey, membersKeys[-1], 0)
                self._close_data(f, member, rangedata[-1], 4, lineEnder='}')
            f.write(']\n')
            f.close()

    def rist_generate_ranges_variable_file(self, ip, sessionId, resourceData, fileName, variableName, vMapFile='../resources/config-files/ranges.conf', mode='append', apiVersion=None):
        """ Ranges for variable file
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
        self.rist_create_variable_file_header(fileName, mode)
        resourceTools = RistConnections()
        rangedata = []
        with open(fileName, 'a') as f:
            f.write(variableName + '= [\n')
            for members in resourceData:
                for rangeuri in members['rangeUris']:
                    ipv4_data = resourceTools.get_ipv4_ranges(ip, sessionId, rangeuri, api=apiVersion)
                    rangedata.append(ipv4_data)
            for member in rangedata:
                f.write(' ' * 4 + '{\n')
                for membersKey in membersKeys:
                    if membersKey not in member:
                        continue
                    if re.search('Uri$', membersKey):
                        uriName = str(None)
                        if member[membersKey] is not None:
                            uriName = resourceTools.get_attr_by_uri(ip, sessionId, member[membersKey], api=apiVersion)
                        f.write(' ' * 8 + '"' + membersKey + '": ')
                        f.write('"' + str(uriName) + '"')
                    else:
                        member[membersKey] = self._ascii_encode(member[membersKey])
                        f.write(' ' * 8 + "'" + membersKey + "': ")
                        f.write(str(member[membersKey]))
                    self._close_data(f, membersKey, membersKeys[-1], 0)
                self._close_data(f, member, rangedata[-1], 4, lineEnder='}')
            f.write(']\n')
            f.close()

    def rist_generate_os_deployment_server_variable_file(self, ip, sessionId, resourceData, fileName, variableName, vMapFile='../resources/config-files/os-deployment.conf', mode='append', apiVersion=None):
        """ OS Deployment Server parser for variable file
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
        self.rist_create_variable_file_header(fileName, mode)
        resourceTools = RistConnections()
        mgmt_list = []
        with open(fileName, 'a') as f:
            f.write(variableName + '= [\n')
            for members in resourceData['members']:
                f.write(' ' * 4 + '{\n')
                for membersKey in membersKeys:
                    if membersKey == 'applianceUri':
                        pair = {membersKey: members['primaryActiveAppliance']}
                        members.update(pair)
                    if membersKey not in members:
                        continue
                    if re.search('Uri$', membersKey):
                        uriName = str(None)
                        if members[membersKey] is not None:
                            uriName = resourceTools.get_attr_by_uri(ip, sessionId, members[membersKey], api=apiVersion)
                        f.write(' ' * 8 + "'" + membersKey + "': ")
                        if membersKey == 'mgmtNetworkUri':
                            mgmt_list.append(uriName)
                            f.write(str(mgmt_list))
                        else:
                            f.write("'" + str(uriName) + "'")
                    else:
                        members[membersKey] = self._ascii_encode(members[membersKey])
                        f.write(' ' * 8 + "'" + membersKey + "': ")
                        f.write(str(members[membersKey]))
                    self._close_data(f, membersKey, membersKeys[-1], 0)
                self._close_data(f, members, resourceData['members'][-1], 4, lineEnder='}')
            f.write(']\n')
            f.close()

    def rist_generate_users_variable_file(self, ip, sessionId, resourceData, fileName, variableName, vMapFile='../resources/config-files/users.conf', mode='append', apiVersion=None):
        """ Users parser for variable file
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
        expectedKeys = vConfig.expectedKeys
        expectedVariable = "expected_" + variableName

        self.variable_file_generic_parser(ip, sessionId, resourceData, fileName, variableName, expectedVariable, membersKeys, expectedKeys, mode, apiVersion=apiVersion)

    def rist_generate_sanmanager_variable_file(self, ip, sessionId, resourceData, fileName, variableName, vMapFile='../resources/config-files/san-manager.conf', mode='append', apiVersion=None):
        """ Users parser for variable file
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
        vKeys = {
            'membersKeys': vConfig.membersKeys,
            'expectedKeys': vConfig.expectedKeys,
            'membersDict': vConfig.membersDict,
            'keepUris': vConfig.keepUris,
            'globalNegativeCondDict': vConfig.globalNegativeCondDict,
            'nonglobalNegativeCondDict': vConfig.nonglobalNegativeCondDict
        }
        sanlist = []
        sanData = {}
        credslist = data_variables.get_variables()
        sandata = credslist['san_managers']
        for member in resourceData['members']:
            if member['providerDisplayName'] == 'Direct attach':
                print "Direct Attach SAN Manager"
            else:
                sanlist.append(member)
        sanData['members'] = sanlist
        expectedVariable = "expected_" + variableName
        self.variable_file_generic2_parser(ip, sessionId, sanData, fileName, variableName, expectedVariable, vKeys, mode, apiVersion=apiVersion)

    def rist_generate_ethnets_variable_file(self, ip, sessionId, resourceData, fileName, variableName, vMapFile='../resources/config-files/ethernet.conf', mode='append', apiVersion=None):
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
        expectedKeys = vConfig.expectedKeys
        expectedVariable = "expected_" + variableName
        normal_nets = []
        normal_networks = {}
        associate_nets = []
        associate_networks = {}
        for members in resourceData['members']:
            if members['subnetUri']:
                associate_nets.append(members)
            else:
                normal_nets.append(members)
        normal_networks['members'] = normal_nets
        associate_networks['members'] = associate_nets
        self.variable_file_generic_parser(ip, sessionId, normal_networks, fileName, variableName, expectedVariable, membersKeys, expectedKeys, mode, apiVersion=apiVersion)
        subnetVariable = "i3s_networks"
        expectedsubnetVariable = "expected_" + subnetVariable
        self.variable_file_generic_parser(ip, sessionId, associate_networks, fileName, subnetVariable, expectedsubnetVariable, membersKeys, expectedKeys, mode, apiVersion=apiVersion)
        self.rist_generate_subnet_networks_file(ip, sessionId, associate_networks, fileName, 'subnet_association', mode, apiVersion=apiVersion)

    def rist_generate_subnet_networks_file(self, ip, sessionId, resourceData, fileName, variableName, mode='append', apiVersion=None):
        newKeys = ["type", "name", "subnetUri"]
        expectedsubnet = None
        resourceTools = RistConnections()
        with open(fileName, 'a') as f:
            f.write(variableName + ' = [\n')
            for member in resourceData['members']:
                f.write(' ' * 4 + '{\n')
                for membersKey in newKeys:
                    if membersKey not in member:
                        continue
                    if re.search('Uri$', membersKey):
                        uriName = str(None)
                        if member[membersKey] is not None:
                            uriName = resourceTools.get_attr_by_uri(ip, sessionId, member[membersKey], api=apiVersion)
                        f.write(' ' * 8 + '"' + membersKey + '": ')
                        f.write('"' + str(uriName) + '"')
                    else:
                        if membersKey == 'type':
                            f.write(' ' * 8 + "'" + 'network type' + "': ")
                            f.write(member[membersKey] + ',\n')
                            continue
                        f.write(' ' * 8 + "'" + membersKey + "': ")
                        f.write(member[membersKey])
                    self._close_data(f, membersKey, newKeys[-1], 0)
                self._close_data(f, member, resourceData['members'][-1], 4, lineEnder='}')
            f.write(']\n')
            f.close()

    def rist_generate_fcnets_variable_file(self, ip, sessionId, resourceData, fileName, variableName, vMapFile='../resources/config-files/fc.conf', mode='append', apiVersion=None):
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
        expectedKeys = vConfig.expectedKeys
        expectedlist = []
        self.rist_create_variable_file_header(fileName, mode)
        resourceTools = RistConnections()
        with open(fileName, 'a') as f:
            f.write(variableName + ' = [\n')
            for members in resourceData['members']:
                f.write(' ' * 4 + '{\n')
                expectedlist.append(' ' * 4 + '{\n')
                for addkey in expectedKeys:
                    expectedlist.append(' ' * 8 + '"' + addkey + '": ')
                    if members[addkey] is not None:
                        if addkey == 'uri':
                            nameuri = resourceTools.add_tagname_to_uri(ip, sessionId, members[addkey], api=apiVersion)
                            expectedlist.append('"' + str(nameuri) + '",\n')
                        else:
                            expectedlist.append('"' + str(members[addkey]) + '",\n')
                    else:
                        expectedlist.append(str(members[addkey]) + ',\n')
                for key in membersKeys:
                    answerlist = ''
                    if re.search('Uri$', key):
                        uriName = str(None)
                        if members[key] is not None:
                            uriName = resourceTools.get_attr_by_uri(ip, sessionId, members[key], api=apiVersion)
                            f.write(' ' * 8 + '"' + key + '": ')
                            f.write('"FCSan:' + str(uriName) + '"')
                            answerlist += ' ' * 8 + '"' + key + '": '
                            answerlist += '"FCSan:' + str(uriName) + '"'
                        else:
                            f.write(' ' * 8 + '"' + key + '": ')
                            f.write(str(None))
                            answerlist += ' ' * 8 + '"' + key + '": '
                            answerlist += str(None)
                    else:
                        if key not in members:
                            continue
                        members[key] = self._ascii_encode(members[key])
                        f.write(' ' * 8 + '"' + key + '": ')
                        f.write(str(members[key]))
                        answerlist += ' ' * 8 + '"' + key + '": '
                        answerlist += str(members[key])

                    expectedlist.append(answerlist)
                    expectedlist.append(self._spaceformat_data(key, membersKeys[-1], 0))
                    self._close_data(f, key, membersKeys[-1], 0)
                expectedlist.append(self._spaceformat_data(members, resourceData['members'][-1], 4, lineEnder='}'))
                self._close_data(f, members, resourceData['members'][-1], 4, lineEnder='}')
            f.write(']\n')
            f.close()
            expectedVarName = "expected_" + variableName
            self._write_data(fileName, expectedVarName, expectedlist)

    def rist_generate_fcoenets_variable_file(self, ip, sessionId, resourceData, fileName, variableName, vMapFile='../resources/config-files/fcoe.conf', mode='append', apiVersion=None):
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
        expectedKeys = vConfig.expectedKeys
        expectedVariable = "expected_" + variableName

        self.variable_file_generic_parser(ip, sessionId, resourceData, fileName, variableName, expectedVariable, membersKeys, expectedKeys, mode, apiVersion=apiVersion)

    def rist_generate_networksets_variable_file(self, ip, sessionId, resourceData, fileName, variableName, vMapFile='../resources/config-files/networksets.conf', mode='append', apiVersion=None):
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
        expectedKeys = vConfig.expectedKeys
        expectedlist = []
        self.rist_create_variable_file_header(fileName, mode)
        with open(fileName, 'a') as f:
            f.write(variableName + ' = [\n')
            resourceTools = RistConnections()
            for members in resourceData['members']:
                f.write(' ' * 4 + '{\n')
                expectedlist.append(' ' * 4 + '{\n')
                for addkey in expectedKeys:
                    expectedlist.append(' ' * 8 + '"' + addkey + '": ')
                    if members[addkey] is not None:
                        if addkey == 'uri':
                            nameuri = resourceTools.add_tagname_to_uri(ip, sessionId, members[addkey], api=apiVersion)
                            expectedlist.append('"' + str(nameuri) + '",\n')
                        else:
                            expectedlist.append('"' + str(members[addkey]) + '",\n')
                    else:
                        expectedlist.append(str(members[addkey]) + ',\n')
                # get the membersKeys listed above
                for membersKey in membersKeys:
                    answerlist = ''
                    if re.search('Uri$', membersKey):
                        # string uri
                        if members[membersKey] is not None:
                            uriName = '"' + resourceTools.get_attr_by_uri(ip, sessionId, members[membersKey]) + '"'
                        else:
                            uriName = str(None)
                        f.write(' ' * 8 + '"' + membersKey + '": ')
                        f.write(uriName)
                        answerlist += ' ' * 8 + '"' + membersKey + '": '
                        if members[membersKey] is not None:
                            answerlist += '"' + resourceTools.add_tagname_to_uri(ip, sessionId, members[membersKey]) + '"'
                        else:
                            answerlist += str(None)
                        expectedlist.append(answerlist)
                        self._close_data(f, membersKey, membersKeys[-1], 0)
                        expectedlist.append(self._spaceformat_data(membersKey, membersKeys[-1], 0))
                    elif re.search('Uris$', membersKey):
                        # list of uris will be replaced with the networkUri->name
                        f.write(' ' * 8 + '"' + membersKey + '": [\n')
                        answerlist += ' ' * 8 + '"' + membersKey + '": [\n'
                        expectedlist.append(answerlist)
                        if len(members[membersKey]) > 0:
                            for rawUri in members[membersKey]:
                                self._close_data(f, rawUri, members[membersKey][-1], 12, lineEnder='"' + resourceTools.get_attr_by_uri(ip, sessionId, rawUri) + '"')
                                expectedlist.append(self._spaceformat_data(rawUri, members[membersKey][-1], 12, lineEnder='"' + resourceTools.add_tagname_to_uri(ip, sessionId, rawUri) + '"'))
                        self._close_data(f, membersKey, membersKeys[-1], 8, lineEnder=']')
                        expectedlist.append(self._spaceformat_data(membersKey, membersKeys[-1], 8, lineEnder=']'))
                    else:
                        members[membersKey] = self._ascii_encode(members[membersKey])
                        f.write(' ' * 8 + '"' + membersKey + '": ' + str(members[membersKey]))
                        answerlist += ' ' * 8 + '"' + membersKey + '": ' + str(members[membersKey])
                        expectedlist.append(answerlist)
                        expectedlist.append(self._spaceformat_data(membersKey, membersKeys[-1], 0))
                        self._close_data(f, membersKey, membersKeys[-1], 0)
                self._close_data(f, members, resourceData['members'][-1], 4, lineEnder='}')
                expectedlist.append(self._spaceformat_data(members, resourceData['members'][-1], 4, lineEnder='}'))
            f.write(']\n')
            f.close()
            expectedVarName = "expected_" + variableName
            self._write_data(fileName, expectedVarName, expectedlist)

    def rist_generate_lig_variable_file(self, ip, sessionId, resourceData, fileName, variableName, vMapFile='../resources/config-files/lig-payload.conf', mode='append', apiVersion=None):
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
        expectedKeys = vConfig.expectedKeys
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

        expectedlist = []
        self.rist_create_variable_file_header(fileName, mode)
        with open(fileName, 'a') as f:
            f.write(variableName + ' = [\n')
            resourceTools = RistConnections()
            ligInstance = RistLogicalInterconnectGroup()
            for members in resourceData['members']:
                f.write(' ' * 4 + '{\n')
                expectedlist.append(' ' * 4 + '{\n')
                for addkey in expectedKeys:
                    expectedlist.append(' ' * 8 + '"' + addkey + '": ')
                    if members[addkey] is not None:
                        if addkey == 'uri':
                            nameuri = resourceTools.add_tagname_to_uri(ip, sessionId, members[addkey], api=apiVersion)
                            expectedlist.append('"' + str(nameuri) + '",\n')
                        else:
                            expectedlist.append('"' + str(members[addkey]) + '",\n')
                    else:
                        expectedlist.append(str(members[addkey]) + ',\n')
                for membersKey in membersKeys:
                    answerlist = ''
                    if membersKey in membersDict:
                        # membersKey is listed in membersDict
                        # build the dict/list
                        f.write(' ' * 8 + '"' + membersKey + '": ' + dataTypeToSym[membersDict[membersKey + '_type'] + '_begin'] + '\n')
                        # Don't capture interconnectmaptemplate  in expected value since verification looking for a particular order each time,
                        if membersKey == 'interconnectMapTemplate' or membersKey == 'uplinkSets':
                            print "INTERCONNECTMAPTEMPLATE is found"
                        else:
                            answerlist += ' ' * 8 + '"' + membersKey + '": ' + dataTypeToSym[membersDict[membersKey + '_type'] + '_begin'] + '\n'
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
                                            uriName = resourceTools.get_attr_by_uri(ip, sessionId, listOfDictValue[membersDictKey], api=apiVersion)
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
                                            uriName = resourceTools.get_attr_by_uri(ip, sessionId, rawUri, api=apiVersion)
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
                                                                    for i, (tkey, tvalue) in self.rist_annotate(tmpDict.iteritems()):
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
                                                    for i, (tkey, tvalue) in self.rist_annotate(tmpDict.iteritems()):
                                                        strToAppend = '"' + tkey + '": "' + tvalue + '"'
                                                        if i == '-1':
                                                            tmpList.append(strToAppend + '\n')
                                                        else:
                                                            tmpList.append(strToAppend + ',\n')
                                            # write the list here (this is to conform with exiting 2.0 variable file formatting)

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
                                                    uriName = resourceTools.get_attr_by_uri(ip, sessionId, level2Value[level2Key], api=apiVersion)
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
                        else:
                            # anything else outside type listOfDict
                            for membersDictKey in membersDict[membersKey]:
                                # grab whatever listed membersDict[membersKey]
                                members[membersKey][membersDictKey] = self._ascii_encode(members[membersKey][membersDictKey])
                                f.write(' ' * 12 + '"' + membersDictKey + '": ')
                                f.write(str(members[membersKey][membersDictKey]))
                                answerlist += ' ' * 12 + '"' + membersDictKey + '": '
                                answerlist += str(members[membersKey][membersDictKey])
                                answerlist += self._spaceformat_data(membersDictKey, membersDict[membersKey][-1], 0)
                                self._close_data(f, membersDictKey, membersDict[membersKey][-1], 0)
                        f.write(' ' * 8 + dataTypeToSym[membersDict[membersKey + '_type'] + '_end'])
                        if membersKey not in ['interconnectMapTemplate', 'uplinkSets']:
                            answerlist += ' ' * 8 + dataTypeToSym[membersDict[membersKey + '_type'] + '_end']
                    else:
                        # membersKey has immediate value (not a list or dict key of something else)
                        members[membersKey] = self._ascii_encode(members[membersKey])
                        f.write(' ' * 8 + '"' + membersKey + '": ')
                        f.write(str(members[membersKey]))
                        answerlist += ' ' * 8 + '"' + membersKey + '": '
                        answerlist += str(members[membersKey])
                    expectedlist.append(answerlist)
                    # if membersKey != 'interconnectMapTemplate' or membersKey != 'uplinkSets':
                    if membersKey not in ['interconnectMapTemplate', 'uplinkSets']:
                        expectedlist.append(self._spaceformat_data(membersKey, membersKeys[-1], 0))
                    self._close_data(f, membersKey, membersKeys[-1], 0)
                expectedlist.append(self._spaceformat_data(members, resourceData['members'][-1], 4, lineEnder='}'))
                self._close_data(f, members, resourceData['members'][-1], 4, lineEnder='}')
            f.write(']\n')
            f.close()
            expectedVarName = "expected_" + "lig"
            self._write_data(fileName, expectedVarName, expectedlist)

    def rist_generate_sas_lig_variable_file(self, ip, sessionId, resourceData, fileName, variableName, vMapFile='../resources/config-files/sas-lig.conf', mode='append', apiVersion=None):
        """ sas lig parser for variable file
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
        expectedKeys = vConfig.expectedKeys
        interconnectMapTemplateKeys = vConfig.interconnectMapTemplateKeys
        interconnectMapEntryTemplatesKeys = vConfig.interconnectMapEntryTemplatesKeys
        logicalLocationDict = vConfig.logicalLocationDict
        membersDict = vConfig.membersDict
        dataTypeToSym = vConfig.dataTypeToSym
        customDict = vConfig.customDict
        icmPorts = {}
        bayNumber = 0

        self.rist_create_variable_file_header(fileName, mode)
        expectedlist = []
        with open(fileName, 'a') as f:
            f.write(variableName + ' = [\n')
            resourceTools = RistConnections()
            ligInstance = RistLogicalInterconnectGroup()
            for members in resourceData['members']:
                f.write(' ' * 4 + '{\n')
                expectedlist.append(' ' * 4 + '{\n')
                for addkey in expectedKeys:
                    expectedlist.append(' ' * 8 + '"' + addkey + '": ')
                    if members[addkey] is not None:
                        if addkey == 'uri':
                            nameuri = resourceTools.add_tagname_to_uri(ip, sessionId, members[addkey], api=apiVersion)
                            expectedlist.append('"' + str(nameuri) + '",\n')
                        else:
                            expectedlist.append('"' + str(members[addkey]) + '",\n')
                    else:
                        expectedlist.append(str(members[addkey]) + ',\n')
                for membersKey in membersKeys:
                    answerlist = ''
                    if membersKey in membersDict:
                        # membersKey is listed in membersDict
                        # build the dict/list
                        f.write(' ' * 8 + '"' + membersKey + '": ' + dataTypeToSym[membersDict[membersKey + '_type'] + '_begin'] + '\n')
                        if membersKey != 'interconnectMapTemplate':
                            answerlist += ' ' * 8 + '"' + membersKey + '": ' + dataTypeToSym[membersDict[membersKey + '_type'] + '_begin'] + '\n'
                        if membersDict[membersKey + '_type'] == 'listOfDict':
                            # use membersKey in getting the values listed in membersDict[membersKey] list of dictionaries
                            for listOfDictValue in members[membersKey]:
                                f.write(' ' * 8 + '{\n')
                                answerlist += ' ' * 8 + '{\n'
                                # get the listed key from each index of list of dictionaries
                                for membersDictKey in membersDict[membersKey]:
                                    if re.search('Uri$', membersDictKey):
                                        # string uri
                                        uriName = None
                                        if listOfDictValue[membersDictKey] is not None:
                                            uriName = resourceTools.get_attr_by_uri(ip, sessionId, listOfDictValue[membersDictKey], api=apiVersion)
                                        uriName = self._ascii_encode(uriName)
                                        f.write(' ' * 12 + '"' + membersDictKey + '": ' + str(uriName))
                                        self._close_data(f, membersDictKey, members[membersKey][-1], 0)
                                        answerlist += ' ' * 12 + '"' + membersDictKey + '": ' + str(uriName)
                                        answerlist += self._spaceformat_data(membersDictKey, members[membersKey][-1], 0)
                                        continue
                                    elif re.search('Uris$', membersDictKey):
                                        # list of uris
                                        f.write(' ' * 12 + '"' + membersDictKey + '": [\n')
                                        for rawUri in listOfDictValue[membersDictKey]:
                                            # TODO: Came across a config with some URI lookup returned error/None/null. I need to figure what data the library
                                            # expect when this happen. For now, leaving it 'empty'/"" so the library won't process it
                                            uriName = resourceTools.get_attr_by_uri(ip, sessionId, rawUri, api=apiVersion)
                                            uriName = self._ascii_encode(uriName)
                                            if uriName is None:
                                                uriName = ""
                                            f.write(' ' * 16 + str(uriName))
                                            self._close_data(f, rawUri, listOfDictValue[membersDictKey][-1], 0)
                                            answerlist += ' ' * 16 + str(uriName)
                                            answerlist += self._spaceformat_data(rawUri, listOfDictValue[membersDictKey][-1], 0)
                                        f.write(' ' * 12 + '],\n')
                                        answerlist += ' ' * 12 + '],\n'
                                        continue
                                    # checking for level2 list of dict
                                    if membersDict.get(membersDictKey + '_type') == 'listOfDict':
                                        # create/write the list
                                        if listOfDictValue[membersDictKey] is None:
                                            f.write(' ' * 12 + '"' + membersDictKey + '": None\n')
                                            answerlist += ' ' * 12 + '"' + membersDictKey + '": None\n'
                                            continue
                                        else:
                                            f.write(' ' * 12 + '"' + membersDictKey + '": [\n')
                                            answerlist += ' ' * 12 + '"' + membersDictKey + '": [\n'

                                        for level2Value in listOfDictValue[membersDictKey]:
                                            # compose dictionary
                                            f.write(' ' * 16 + '{\n')
                                            answerlist += ' ' * 16 + '{\n'
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
                                                                    for i, (tkey, tvalue) in self.rist_annotate(tmpDict.iteritems()):
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
                                                    answerlist += ' ' * 20 + '"' + modLevel2Key + '": ' + level2Value[level2Key]
                                                    answerlist += self._spaceformat_data(level2Key, listOfDictValue[membersDictKey][-1], 0)
                                            # write the list here (this is to conform with exiting 2.0 variable file formatting)
                                            [f.write(' ' * 20 + k) for k in tmpList if k]
                                            self._close_data(f, level2Value, listOfDictValue[membersDictKey][-1], 16, lineEnder='}')
                                            for k in tmpList:
                                                if k:
                                                    answerlist += ' ' * 20 + k
                                            answerlist += self._spaceformat_data(level2Value, listOfDictValue[membersDictKey][-1], 16, lineEnder='}')
                                        # end list
                                        self._close_data(f, membersDictKey, members[membersKey][-1], 12, lineEnder=']')
                                        answerlist += self._spaceformat_data(membersDictKey, members[membersKey][-1], 12, lineEnder=']')
                                    elif membersDict.get(membersDictKey + '_type') == 'modListOfDict':
                                        # create/write the list
                                        if listOfDictValue[membersDictKey] is None:
                                            f.write(' ' * 12 + '"' + membersDictKey + '": None\n')
                                            answerlist += ' ' * 12 + '"' + membersDictKey + '": None\n'

                                            continue
                                        else:
                                            # compose dictionary
                                            f.write(' ' * 12 + '"' + membersDictKey + '": {\n')
                                            answerlist += ' ' * 12 + '"' + membersDictKey + '": {\n'
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
                                                    for i, (tkey, tvalue) in self.rist_annotate(tmpDict.iteritems()):
                                                        strToAppend = '"' + tkey + '": "' + tvalue + '"'
                                                        if i == '-1':
                                                            tmpList.append(strToAppend + '\n')
                                                        else:
                                                            tmpList.append(strToAppend + ',\n')
                                            # write the list here (this is to conform with exiting 2.0 variable file formatting)
                                            [f.write(' ' * 16 + k) for k in tmpList if k]
                                            for k in tmpList:
                                                if k:
                                                    answerlist += ' ' * 16 + k
                                            # end list
                                            answerlist += self._spaceformat_data(membersDictKey, members[membersKey][-1], 12, lineEnder='}')
                                            self._close_data(f, membersDictKey, members[membersKey][-1], 12, lineEnder='}')
                                    else:
                                        # immediate second-level stuff
                                        listOfDictValue[membersDictKey] = self._ascii_encode(listOfDictValue[membersDictKey])
                                        f.write(' ' * 12 + '"' + membersDictKey + '": ')
                                        f.write(str(listOfDictValue[membersDictKey]))
                                        self._close_data(f, membersDictKey, members[membersKey][-1], 0)
                                        answerlist += ' ' * 12 + '"' + membersDictKey + '": '
                                        answerlist += str(listOfDictValue[membersDictKey])
                                        answerlist += self._spaceformat_data(membersDictKey, members[membersKey][-1], 0)
                                self._close_data(f, listOfDictValue, members[membersKey][-1], 8, lineEnder='}')
                                answerlist += self._spaceformat_data(listOfDictValue, members[membersKey][-1], 8, lineEnder='}')
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
                                                    uriName = resourceTools.get_attr_by_uri(ip, sessionId, level2Value[level2Key], api=apiVersion)
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
                                                        print "level3Value", level3Value
                                                        for level3Key in membersDict[level2Key]:
                                                            if isinstance(membersDict[level2Key][level3Key], list):
                                                                # it's list of dictionaries
                                                                # loop thru the likes of locationEntries list values
                                                                for level4Value in level2Value[level2Key][level3Value]:
                                                                    # loop thru each defined keys off membersDict[level2Key][level3Key] list, get the values, and write to file
                                                                    for level5Key in membersDict[level2Key][level3Key]:
                                                                        # added to conform with the exfisting 2.0 variable type format supported by library
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
                                        print "VALUE OF TEMP LIST", tmpList
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
                        else:
                            # anything else outside type listOfDict
                            for membersDictKey in membersDict[membersKey]:
                                # grab whatever listed membersDict[membersKey]
                                members[membersKey][membersDictKey] = self._ascii_encode(members[membersKey][membersDictKey])
                                f.write(' ' * 12 + '"' + membersDictKey + '": ')
                                f.write(str(members[membersKey][membersDictKey]))
                                self._close_data(f, membersDictKey, membersDict[membersKey][-1], 0)
                                answerlist += ' ' * 12 + '"' + membersDictKey + '": '
                                answerlist += str(members[membersKey][membersDictKey])
                                answerlist += self._spaceformat_data(membersDictKey, membersDict[membersKey][-1], 0)

                        f.write(' ' * 8 + dataTypeToSym[membersDict[membersKey + '_type'] + '_end'])
                        if membersKey != 'interconnectMapTemplate':
                            answerlist += ' ' * 8 + dataTypeToSym[membersDict[membersKey + '_type'] + '_end']
                    else:
                        # membersKey has immediate value (not a list or dict key of something else)
                        members[membersKey] = self._ascii_encode(members[membersKey])
                        f.write(' ' * 8 + '"' + membersKey + '": ')
                        f.write(str(members[membersKey]))
                        answerlist += ' ' * 8 + '"' + membersKey + '": '
                        answerlist += str(members[membersKey])
                    expectedlist.append(answerlist)
                    self._close_data(f, membersKey, membersKeys[-1], 0)
                    if membersKey != 'interconnectMapTemplate':
                        expectedlist.append(self._spaceformat_data(membersKey, membersKeys[-1], 0))
                self._close_data(f, members, resourceData['members'][-1], 4, lineEnder='}')
                expectedlist.append(self._spaceformat_data(members, resourceData['members'][-1], 4, lineEnder='}'))
            f.write(']\n')
            f.close()
            expectedVarName = "expected_" + variableName
            self._write_data(fileName, expectedVarName, expectedlist)

    def rist_generate_encgrp_variable_file(self, ip, sessionId, resourceData, fileName, variableName, vMapFile='../resources/config-files/enclosure-group.conf', mode='append', apiVersion=None):
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
            'expectedKeys': vConfig.expectedKeys,
            'interconnectBayMappingsKeys': vConfig.interconnectBayMappingsKeys,
            'membersDict': vConfig.membersDict,
            'keepUris': vConfig.keepUris,
            'globalNegativeCondDict': vConfig.globalNegativeCondDict,
            'nonglobalNegativeCondDict': vConfig.nonglobalNegativeCondDict
        }
        expectedVariable = "expected_" + variableName
        self.variable_file_generic2_parser(ip, sessionId, resourceData, fileName, variableName, expectedVariable, vKeys, mode, apiVersion=apiVersion)

    def rist_generate_le_variable_file(self, ip, sessionId, resourceData, fileName, variableName, vMapFile='../resources/config-files/le.conf', mode='append', apiVersion=None):
        """ Logical enclosure parser for variable file
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
        expectedKeys = vConfig.expectedKeys
        expectedlist = []
        listUri = {}
        self.rist_create_variable_file_header(fileName, mode)
        with open(fileName, 'a') as f:
            f.write(variableName + ' = [\n')
            resourceTools = RistConnections()
            for members in resourceData['members']:
                f.write(' ' * 4 + '{\n')
                expectedlist.append(' ' * 4 + '{\n')
                for addkey in expectedKeys:
                    expectedlist.append(' ' * 8 + '"' + addkey + '": ')
                    if members[addkey] is not None:
                        if re.search('Uri$', addkey) or re.search('uri$', addkey):
                            nameuri = resourceTools.add_tagname_to_uri(ip, sessionId, members[addkey], api=apiVersion)
                            if nameuri is not None:
                                expectedlist.append('"' + str(nameuri) + '",\n')
                        else:
                            if str(members[addkey]).isdigit() or '[' in members[addkey]:
                                expectedlist.append(str(members[addkey]) + ',\n')
                            else:
                                expectedlist.append('"' + str(members[addkey]) + '",\n')
                    else:
                        expectedlist.append(str(members[addkey]) + ',\n')
                # get the membersKeys listed above
                for membersKey in membersKeys:
                    answerlist = ''
                    if re.search('Uri$', membersKey):
                        # string uri
                        if members[membersKey] is not None:
                            uriName = resourceTools.add_tagname_to_uri(ip, sessionId, members[membersKey], api=apiVersion)
                        else:
                            uriName = str(None)
                        f.write(' ' * 8 + '"' + membersKey + '": ')
                        f.write('"' + uriName + '"')
                        self._close_data(f, membersKey, membersKeys[-1], 0)
                        answerlist += ' ' * 8 + '"' + membersKey + '": '
                        answerlist += '"' + uriName + '"'
                        answerlist += self._spaceformat_data(membersKey, membersKeys[-1], 0)
                    elif re.search('Uris$', membersKey):
                        # list of uris will be replaced with the networkUri->name
                        f.write(' ' * 8 + '"' + membersKey + '": [\n')
                        answerlist += ' ' * 8 + '"' + membersKey + '": [\n'
                        # Get the bay number of Potash Module and then sort it to get enclosures in order.
                        for rawUri in members[membersKey]:
                            baynumber = resourceTools.get_interconnect_bay(ip, sessionId, rawUri, api=apiVersion)
                            if baynumber:
                                listUri[baynumber] = rawUri
                            else:
                                print "It is none value"
                                baynumber = 9999999
                                listUri[baynumber] = rawUri
                        orderlist = collections.OrderedDict(sorted(listUri.items()))
                        for k, encUri in orderlist.items():
                            self._close_data(f, str(encUri), members[membersKey][-1], 12, lineEnder='"' + resourceTools.add_tagname_to_uri(ip, sessionId, encUri, api=apiVersion) + '"')
                            answerlist += self._spaceformat_data(str(encUri), members[membersKey][-1], 12, lineEnder='"' + resourceTools.add_tagname_to_uri(ip, sessionId, encUri, api=apiVersion) + '"')
                        self._close_data(f, membersKey, membersKeys[-1], 8, lineEnder=']')
                        answerlist += self._spaceformat_data(membersKey, membersKeys[-1], 8, lineEnder=']')
                    else:
                        members[membersKey] = self._ascii_encode(members[membersKey])
                        f.write(' ' * 8 + '"' + membersKey + '": ' + str(members[membersKey]))
                        self._close_data(f, membersKey, membersKeys[-1], 0)
                        answerlist += ' ' * 8 + '"' + membersKey + '": ' + str(members[membersKey])
                        answerlist += self._spaceformat_data(membersKey, membersKeys[-1], 0)
                    expectedlist.append(answerlist)
                self._close_data(f, members, resourceData['members'][-1], 4, lineEnder='}')
                expectedlist.append(self._spaceformat_data(members, resourceData['members'][-1], 4, lineEnder='}'))
            f.write(']\n')
            f.close()
            expectedVarName = "expected_" + variableName
            self._write_data(fileName, expectedVarName, expectedlist)

    def rist_generate_enclosures_variable_file(self, ip, sessionId, resourceData, fileName, variableName, vMapFile='../resources/config-files/enclosures.conf', mode='append', build_type=None, apiVersion=None):
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
        print "build_type", build_type
        oneview_type = re.match('Tbird|c7000', build_type, re.IGNORECASE)
        if oneview_type:
            if oneview_type.group() == 'Tbird' or oneview_type.group() == 'TBIRD':
                print " It is Tbird appliance", oneview_type.group()
                vMapFile = "../resources/config-files/enclosures.conf"
                with open(vMapFile, 'r') as r:
                    vConfig = imp.new_module('data')
                    exec(r.read(), vConfig.__dict__)
                vKeys = {
                    'membersKeys': vConfig.membersKeys,
                    'membersDict': vConfig.membersDict,
                    'keepUris': vConfig.keepUris,
                    'globalNegativeCondDict': vConfig.globalNegativeCondDict,
                    'nonglobalNegativeCondDict': vConfig.nonglobalNegativeCondDict
                }
                for members in resourceData['members']:
                    if 'state' in members:
                        if members['state'] == 'Monitored':
                            varName = 'monitored_' + variableName
                        else:
                            varName = 'configured_' + variableName
                expectedVariable = None
                self.variable_file_generic2_parser(ip, sessionId, resourceData, fileName, varName, expectedVariable, vKeys, mode, apiVersion=apiVersion)
            elif oneview_type.group() == 'c7000' or oneview_type.group() == 'C7000':
                print "It is C7000 Appliance"
                vMapFile = "../resources/config-files/enclosures-c7000.conf"
                with open(vMapFile, 'r') as r:
                    vConfig = imp.new_module('data')
                    exec(r.read(), vConfig.__dict__)
                membersKeys = vConfig.membersKeys
                expectedKeys = vConfig.expectedKeys
                expectedVariable = 'expected_' + variableName
                self.variable_file_generic_parser(ip, sessionId, resourceData, fileName, variableName, expectedVariable, membersKeys, expectedKeys, mode, apiVersion=apiVersion)
        else:
            print "INVALID BUILDTYPE"
            logger.warn("Invalid Build type to capture Enclosures")

    def rist_generate_servers_variable_file(self, ip, sessionId, resourceData, fileName, variableName, vMapFile='../resources/config-files/servers.conf', mode='append', apiVersion=None):
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
        expectedKeys = None
        expectedVariable = None

        self.variable_file_generic_parser(ip, sessionId, resourceData, fileName, variableName, expectedVariable, membersKeys, expectedKeys, mode, apiVersion=apiVersion)

    def rist_profiles_from_templates_variable_file(self, ip, sessionId, resourceData, fileName, variableName, vMapFile='../resources/config-files/profiles-cifit.conf', mode='append', CIFIT_TYPE_CONV=True, apiVersion=None):
        profiles_template = {}
        profiles_template['members'] = resourceData
        expectedVariable = "expected_" + variableName
        self.rist_generate_profiles_ofvartypes_variable_file(ip, sessionId, profiles_template, fileName, variableName, vMapFile='../resources/config-files/profiles-cifit.conf', mode='append', CIFIT_TYPE_CONV=False, apiVersion=apiVersion)

    def rist_generate_profiles_variable_file(self, ip, sessionId, resourceData, fileName, variableName, vMapFile='../resources/config-files/profiles-cifit.conf', mode='append', CIFIT_TYPE_CONV=False, apiVersion=None):
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

        resource_san = []
        resource_withoutsan = []
        profiles_from_template = []
        profiles = []
        sanProfileData = {}
        withoutsanProfileData = {}
        print "Count of members", resourceData['count']
        for member in resourceData['members']:
            print member['name']
            if member['serverProfileTemplateUri']:
                print "Profile is created from template"
                profiles_from_template.append(member)
            else:
                if member['sanStorage']['manageSanStorage']:
                    print "profile has SAN", member['name']
                    resource_san.append(member)
                else:
                    resource_withoutsan.append(member)

        sanProfileData['members'] = resource_san
        withoutsanProfileData['members'] = resource_withoutsan

        if len(profiles_from_template) > 0 and variableName == 'server_profiles_from_spt':
            self.rist_profiles_from_templates_variable_file(ip, sessionId, profiles_from_template, fileName, variableName, vMapFile='../resources/config-files/profiles-cifit.conf', mode='append', CIFIT_TYPE_CONV=False, apiVersion=apiVersion)
        elif variableName == 'server_profile_with_storage':
            self.rist_generate_profiles_ofvartypes_variable_file(ip, sessionId, sanProfileData, fileName, variableName, vMapFile='../resources/config-files/profiles-cifit.conf', mode='append', CIFIT_TYPE_CONV=False, apiVersion=apiVersion)
        elif variableName == 'server_profiles':
            expectedVariable = "expected_" + variableName
            self.rist_generate_profiles_ofvartypes_variable_file(ip, sessionId, withoutsanProfileData, fileName, variableName, vMapFile='../resources/config-files/profiles-cifit.conf', mode='append', CIFIT_TYPE_CONV=False, apiVersion=apiVersion)
        else:
            print "Variable name is not defined properly"

    def rist_generate_profiles_ofvartypes_variable_file(self, ip, sessionId, resourceData, fileName, variableName, vMapFile='../resources/config-files/profiles-cifit.conf', mode='append', CIFIT_TYPE_CONV=False, apiVersion=None):
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
        membersKeys = vConfig.membersKeys
        expectedKeys = vConfig.expectedKeys
        connectionsKeys = vConfig.connectionsKeys
        bootKeys = vConfig.bootKeys
        bootModeKeys = vConfig.bootModeKeys
        firmwareKeys = vConfig.firmwareKeys
        biosKeys = vConfig.biosKeys
        localStorageKeys = vConfig.localStorageKeys
        sanStorageKeys = vConfig.sanStorageKeys
        volumeAttachmentsKeys = vConfig.volumeAttachmentsKeys
        storagePathsKeys = vConfig.storagePathsKeys
        membersDict = vConfig.membersDict
        globalNegativeCondDict = vConfig.globalNegativeCondDict
        nonglobalNegativeCondDict = vConfig.nonglobalNegativeCondDict
        dataTypeToSym = vConfig.dataTypeToSym
        self.rist_create_variable_file_header(fileName, mode)
        expectedlist = []
        with open(fileName, 'a') as f:
            f.write(variableName + ' = [\n')
            resourceTools = RistConnections()
            for members in resourceData['members']:
                global bootflag
                bootflag = 1
                f.write(' ' * 4 + '{\n')
                expectedlist.append(' ' * 4 + '{\n')
                if variableName == 'server_profiles_from_spt' or variableName == 'server_profiles':
                    if 'hostOSType' not in members['sanStorage']:
                        membersDict['sanStorage'].remove('hostOSType')
                    if 'enclosureUri' in membersKeys:
                        membersKeys.remove('enclosureUri')
                    if variableName == 'server_profiles_from_spt':
                        f.write(' ' * 8 + '"serverProfileTemplateUri": ')
                        f.write('"' + resourceTools.add_tagname_to_uri(ip, sessionId, members['serverProfileTemplateUri'], api=apiVersion) + '",\n')
                for addkey in expectedKeys:
                    expectedlist.append(' ' * 8 + '"' + addkey + '": ')
                    if members[addkey] is not None:
                        if re.search('Uri$', addkey) or re.search('uri$', addkey):
                            if addkey == 'serverHardwareTypeUri':
                                nameuri = resourceTools.get_mezz_model_by_shtname(ip, sessionId, members[addkey], api=apiVersion)
                            else:
                                nameuri = resourceTools.add_tagname_to_uri(ip, sessionId, members[addkey], api=apiVersion)
                            if nameuri is not None:
                                expectedlist.append('"' + str(nameuri) + '",\n')
                        else:
                            if str(members[addkey]).isdigit() or '[' in members[addkey]:
                                expectedlist.append(str(members[addkey]) + ',\n')
                            else:
                                expectedlist.append('"' + str(members[addkey]) + '",\n')
                    else:
                        expectedlist.append(str(members[addkey]) + ',\n')
                for item in members['localStorage']['controllers']:
                    if 'logicalDrives' in item:
                        print "drivenumber is found"
                        if item['logicalDrives']:
                            map(lambda d: d.pop('driveNumber'), item['logicalDrives'])
                    else:
                        print "ITEM NAME", item
                for item in members['localStorage']['sasLogicalJBODs']:
                    if 'sasLogicalJBODUri' in item:
                        print "sasLogicalJBODUri is found"
                        item.pop('sasLogicalJBODUri', None)
                    else:
                        print "ITEM NAME", item
                for membersKey in membersKeys:
                    answerlist = ''
                    if membersKey in membersDict:
                        # membersKey is listed in membersDict
                        # build the dict/list
                        if members[membersKey] is not None:
                            f.write(' ' * 8 + '"' + membersKey + '": ' + dataTypeToSym[membersDict[membersKey + '_type'] + '_begin'] + '\n')
                            answerlist += ' ' * 8 + '"' + membersKey + '": ' + dataTypeToSym[membersDict[membersKey + '_type'] + '_begin'] + '\n'
                        else:
                            f.write(' ' * 8 + '"' + membersKey + '": ')
                            answerlist += ' ' * 8 + '"' + membersKey + '": '
                        if membersDict[membersKey + '_type'] == 'listOfDict':
                            # use membersKey in getting the values listed in membersDict[membersKey] list of dictionaries
                            for listOfDictValue in members[membersKey]:
                                print "listOfDictValue", listOfDictValue
                                f.write(' ' * 12 + '{\n')
                                answerlist += ' ' * 12 + '{\n'
                                # get the listed key from each index of list of dictionaries
                                for membersDictKey in membersDict[membersKey]:
                                    if re.search('Uri$', membersDictKey):
                                        # string uri
                                        uriName = str(None)
                                        if listOfDictValue[membersDictKey] is not None:
                                            uriName = resourceTools.add_tagname_to_uri(ip, sessionId, listOfDictValue[membersDictKey], api=apiVersion)
                                        uriName = self._ascii_encode(uriName)
                                        f.write(' ' * 16 + '"' + membersDictKey + '": ' + str(uriName))
                                        self._close_data(f, membersDictKey, members[membersKey][-1], 0)
                                        answerlist += ' ' * 16 + '"' + membersDictKey + '": ' + str(uriName)
                                        answerlist += self._spaceformat_data(membersDictKey, members[membersKey][-1], 0)
                                        continue
                                    if membersDictKey == 'mac':
                                        listOfDictValue[membersDictKey] = '""'
                                    else:
                                        listOfDictValue[membersDictKey] = self._ascii_encode(listOfDictValue[membersDictKey])
                                    f.write(' ' * 16 + '"' + membersDictKey + '": ' + str(listOfDictValue[membersDictKey]))
                                    self._close_data(f, membersDictKey, members[membersKey][-1], 0)
                                    answerlist += ' ' * 16 + '"' + membersDictKey + '": ' + str(listOfDictValue[membersDictKey])
                                    answerlist += self._spaceformat_data(membersDictKey, members[membersKey][-1], 0)
                                self._close_data(f, listOfDictValue, members[membersKey][-1], 12, lineEnder='}')
                                answerlist += self._spaceformat_data(listOfDictValue, members[membersKey][-1], 12, lineEnder='}')
                            # Navya newly added
                            # self._close_data(f, listOfDictValue, members[membersKey][-1], 8, lineEnder=']')
                            # self._close_data(f, membersKey, vKeys['membersKeys'][-1], 8, lineEnder=']')
                        elif membersDict[membersKey + '_type'] == 'modDictListOfDict':
                            # get the listed key from each index of list of dictionaries
                            for membersDictKey in membersDict[membersKey]:
                                # checking for level2 list of dict
                                print "membersDictKey", membersDictKey
                                if membersDictKey in membersDict:
                                    f.write(' ' * 12 + '"' + membersDictKey + '": ' + dataTypeToSym[membersDict[membersDictKey + '_type'] + '_begin'] + '\n')
                                    answerlist += ' ' * 12 + '"' + membersDictKey + '": ' + dataTypeToSym[membersDict[membersDictKey + '_type'] + '_begin'] + '\n'
                                    if membersDict.get(membersDictKey + '_type') == 'listOfDict':
                                        # create/write the list
                                        if members[membersKey][membersDictKey] is None:
                                            continue
                                        beginFlag = 1
                                        for level2Value in members[membersKey][membersDictKey]:
                                            print "level2Value:{}".format(level2Value)
                                            if 'boot' in level2Value and 'bootVolumeSource' in level2Value['boot']:
                                                if level2Value['boot']['bootVolumeSource'] == 'ManagedVolume':
                                                    bootflag = 0
                                                    if 'targets' in level2Value['boot']:
                                                        level2Value['boot'].pop('targets')
                                            print "VALUE of BOOTFLAG:{}".format(bootflag)
                                            # compose dictionary
                                            if beginFlag == 1:
                                                f.write(' ' * 16 + '{\n')
                                                answerlist += ' ' * 16 + '{\n'
                                            tmpList = []
                                            # loop thru list of dict
                                            # Navya:Little tweak to handle
                                            for pos, level2Key in enumerate(membersDict[membersDictKey]):
                                                # this is where the likes of permittedInterconnectTypeUri will be processed
                                                if re.search('Uri$', level2Key):
                                                    # string uri
                                                    uriName = str(None)
                                                    if level2Value[level2Key] is not None:
                                                        uriName = resourceTools.add_tagname_to_uri(ip, sessionId, level2Value[level2Key], api=apiVersion)
                                                    uriName = self._ascii_encode(uriName)
                                                    f.write(' ' * 20 + '"' + level2Key + '": ' + str(uriName))
                                                    f.write(',\n')
                                                    answerlist += ' ' * 20 + '"' + level2Key + '": ' + str(uriName) + ',\n'

                                                # check with membersDict if something was defined
                                                elif level2Key in membersDict and level2Key != 'boot':
                                                    f.write(' ' * 20 + '"' + level2Key + '": ' + dataTypeToSym[membersDict[level2Key + '_type'] + '_begin'] + '\n')
                                                    answerlist += ' ' * 20 + '"' + level2Key + '": ' + dataTypeToSym[membersDict[level2Key + '_type'] + '_begin'] + '\n'
                                                    # another dictionary processing here (the likes of interconnectMapEntryTemplates->logicalLocation->locationEntries)
                                                    if membersDict[level2Key + '_type'] == 'listOfDict':
                                                        # loop thru logicalLocation key value (dict)
                                                        for level3Value in level2Value[level2Key]:
                                                            f.write(' ' * 24 + '{\n')
                                                            answerlist += ' ' * 24 + '{\n'
                                                            print "level3Value:{}".format(level3Value)
                                                            # loop thru level3Value (dictionary value)
                                                            for level3Key in membersDict[level2Key]:
                                                                if level3Key == 'targets':
                                                                    level3Value[level3Key] = []
                                                                else:
                                                                    level3Value[level3Key] = self._ascii_encode(level3Value[level3Key])
                                                                f.write(' ' * 28 + '"' + level3Key + '": ' + str(level3Value[level3Key]))
                                                                f.write(',\n')
                                                                answerlist += ' ' * 28 + '"' + level3Key + '": ' + str(level3Value[level3Key]) + ',\n'
                                                            f.write(' ' * 24 + dataTypeToSym[membersDict[membersKey + '_type'] + '_end'] + ',\n')
                                                            answerlist += ' ' * 24 + dataTypeToSym[membersDict[membersKey + '_type'] + '_end'] + ',\n'
                                                    f.write('\n')
                                                    answerlist += '\n'
                                                    f.write(' ' * 20 + dataTypeToSym[membersDict[level2Key + '_type'] + '_end'] + '\n')
                                                    answerlist += ' ' * 20 + dataTypeToSym[membersDict[level2Key + '_type'] + '_end'] + '\n'
                                                else:
                                                    print "level2Key:{}".format(level2Key)
                                                    # immediate key-value pair here (no complicated data types)
                                                    if level2Key == 'mac':
                                                        print "Here is MAC"
                                                        level2Value[level2Key] = ''
                                                    if level2Key == 'lunType' and level2Value[level2Key] == 'Auto':
                                                        if membersDict[membersDictKey][pos + 1] == 'lun':
                                                            print "Found lun key"
                                                            level2Value[membersDict[membersDictKey][pos + 1]] = None
                                                    level2Value[level2Key] = self._ascii_encode(level2Value[level2Key])
                                                    if level2Value[level2Key] is not None:
                                                        f.write(' ' * 20 + '"' + level2Key + '": ' + str(level2Value[level2Key]) + ',\n')
                                                        if level2Key == 'mac' or level2Key == 'macType':
                                                            print "MACCCC", level2Key, level2Value[level2Key]
                                                        else:
                                                            answerlist += ' ' * 20 + '"' + level2Key + '": ' + str(level2Value[level2Key]) + ',\n'
                                                    else:
                                                        f.write(' ' * 20 + '"' + level2Key + '": ')
                                                        f.write(str(level2Value[level2Key]) + ',\n')
                                                        answerlist += ' ' * 20 + '"' + level2Key + '": '
                                                        answerlist += str(level2Value[level2Key]) + ',\n'
                                            # write the list here (this is to conform with exiting 2.0 variable file formatting)
                                            if any('"type": "None"\n' == k for k in tmpList if k):
                                                beginFlag = 0
                                                continue
                                            else:
                                                beginFlag = 1
                                            [f.write(' ' * 16 + k) for k in tmpList if k]
                                            for k in tmpList:
                                                if k:
                                                    answerlist += ' ' * 16 + k
                                            self._close_data(f, level2Value, members[membersKey][membersDictKey][-1], 16, lineEnder='}')
                                            answerlist += self._spaceformat_data(level2Value, members[membersKey][membersDictKey][-1], 16, lineEnder='}')
                                    #        f.write(' ' * 12 + dataTypeToSym[membersDict[level2Key + '_type'] + '_end'])
                                    # Navya moved it little front
                                    f.write(' ' * 12 + dataTypeToSym[membersDict[membersDictKey + '_type'] + '_end'] + '\n')
                                    answerlist += ' ' * 12 + dataTypeToSym[membersDict[membersDictKey + '_type'] + '_end'] + '\n'
                                else:
                                    # immediate second-level stuff
                                    print "membersDictKey in else", membersDictKey
                                    members[membersKey][membersDictKey] = self._ascii_encode(members[membersKey][membersDictKey])
                                    f.write(' ' * 12 + '"' + membersDictKey + '": ' + str(members[membersKey][membersDictKey]))
                                    answerlist += ' ' * 12 + '"' + membersDictKey + '": ' + str(members[membersKey][membersDictKey])
                                self._close_data(f, membersDictKey, membersDict[membersKey][-1], 0)
                                answerlist += self._spaceformat_data(membersDictKey, membersDict[membersKey][-1], 0)
                        else:
                            if members[membersKey] is not None:  # anything else outside type listOfDict
                                for membersDictKey in membersDict[membersKey]:
                                    # grab whatever listed membersDict[membersKey]
                                    members[membersKey][membersDictKey] = self._ascii_encode(members[membersKey][membersDictKey])
                                    f.write(' ' * 12 + '"' + membersDictKey + '": ')
                                    answerlist += ' ' * 12 + '"' + membersDictKey + '": '
                                    if membersDictKey == 'order':
                                        orderdata = members[membersKey][membersDictKey].strip('[]')
                                        orderlist = list(orderdata.split(','))
                                        f.write('[' + str(orderlist[0]) + ']')
                                        answerlist += '[' + str(orderlist[0]) + ']'
                                    else:
                                        f.write(str(members[membersKey][membersDictKey]))
                                        answerlist += str(members[membersKey][membersDictKey])
                                    self._close_data(f, membersDictKey, membersDict[membersKey][-1], 0)
                                    answerlist += self._spaceformat_data(membersDictKey, membersDict[membersKey][-1], 0)
                            else:
                                f.write('None,\n')
                                answerlist += 'None,\n'
                        if members[membersKey] is not None:
                            f.write(' ' * 8 + dataTypeToSym[membersDict[membersKey + '_type'] + '_end'] + ',\n')
                            answerlist += ' ' * 8 + dataTypeToSym[membersDict[membersKey + '_type'] + '_end'] + ',\n'
                    else:
                        if re.search('Uri$', membersKey):
                            uriName = str(None)
                            if members[membersKey] is not None:
                                if variableName == 'server_profiles_from_spt' and membersKey == 'serverHardwareUri':
                                    uriName = resourceTools.get_attr_by_uri(ip, sessionId, members[membersKey], api=apiVersion)
                                else:
                                    uriName = resourceTools.add_tagname_to_uri(ip, sessionId, members[membersKey], api=apiVersion)
                            f.write(' ' * 8 + '"' + membersKey + '": "' + str(uriName) + '"')
                            answerlist += ' ' * 8 + '"' + membersKey + '": "' + str(uriName) + '"'
                        # check for conditional keys (global)
                        elif globalNegativeCondDict.get(membersKey) is not None and globalNegativeCondDict.get(membersKey) != members[membersKey] and globalNegativeCondDict.get(membersKey + '_' + members[membersKey]) is not None:
                            for k in globalNegativeCondDict.get(membersKey + '_' + members[membersKey]):
                                members[k] = self._ascii_encode(members[k])
                                f.write(' ' * 8 + '"' + k + '": ' + str(members[k]) + ',\n')
                                answerlist += ' ' * 8 + '"' + k + '": ' + str(members[k]) + ',\n'
                            members[membersKey] = self._ascii_encode(members[membersKey])
                            f.write(' ' * 8 + '"' + membersKey + '": ' + str(members[membersKey]))
                            answerlist += ' ' * 8 + '"' + membersKey + '": ' + str(members[membersKey])
                        else:
                            if membersKey not in members:
                                continue
                            if CIFIT_TYPE_CONV is True and membersKey == 'serialNumberType' and members[membersKey] == 'Virtual':
                                members[membersKey] = 'Virtual'
                            members[membersKey] = self._ascii_encode(members[membersKey])
                            f.write(' ' * 8 + '"' + membersKey + '": ' + str(members[membersKey]))
                            answerlist += ' ' * 8 + '"' + membersKey + '": ' + str(members[membersKey])
                        self._close_data(f, membersKey, membersKeys[-1], 0)
                        answerlist += self._spaceformat_data(membersKey, membersKeys[-1], 0)
                    expectedlist.append(answerlist)
                self._close_data(f, members, resourceData['members'][-1], 4, lineEnder='}')
                expectedlist.append(self._spaceformat_data(members, resourceData['members'][-1], 4, lineEnder='}'))
                # Add Attribute back to dictionary
                if 'hostOSType' not in membersDict['sanStorage']:
                    membersDict['sanStorage'].append('hostOSType')
            f.write(']\n')
            f.close()
            expectedVarName = "expected_" + variableName
            self._write_data(fileName, expectedVarName, expectedlist)

    def rist_generate_spt_variable_file(self, ip, sessionId, resourceData, fileName, variableName, vMapFile='../resources/config-files/spt.conf', mode='append', CIFIT_TYPE_CONV=False, apiVersion=None):
        """ profile template parser for variable file
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
        expectedKeys = vConfig.expectedKeys
        connectionSettingsKeys = vConfig.connectionSettingsKeys
        connectionsKeys = vConfig.connectionsKeys
        bootKeys = vConfig.bootKeys
        bootModeKeys = vConfig.bootModeKeys
        firmwareKeys = vConfig.firmwareKeys
        biosKeys = vConfig.biosKeys
        localStorageKeys = vConfig.localStorageKeys
        membersDict = vConfig.membersDict
        globalNegativeCondDict = vConfig.globalNegativeCondDict
        nonglobalNegativeCondDict = vConfig.nonglobalNegativeCondDict
        dataTypeToSym = vConfig.dataTypeToSym

        expectedlist = []
        self.rist_create_variable_file_header(fileName, mode)
        with open(fileName, 'a') as f:
            f.write(variableName + ' = [\n')
            resourceTools = RistConnections()
            for members in resourceData['members']:
                global bootflag
                bootflag = 1
                f.write(' ' * 4 + '{\n')
                expectedlist.append(' ' * 4 + '{\n')
                for addkey in expectedKeys:
                        print "addkey", addkey
                        expectedlist.append(' ' * 8 + '"' + addkey + '": ')
                        print "addkey value", members[addkey]
                        if members[addkey] is not None:
                            if re.search('Uri$', addkey) or re.search('uri$', addkey):
                                nameuri = resourceTools.add_tagname_to_uri(ip, sessionId, members[addkey], api=apiVersion)
                                if nameuri is not None:
                                    expectedlist.append('"' + str(nameuri) + '",\n')
                            else:
                                if '[' in str(members[addkey]) or isinstance(str(members[addkey]), int):
                                    expectedlist.append(str(members[addkey]) + ',\n')
                                else:
                                    print "I AM in last Else", addkey
                                    expectedlist.append('"' + str(members[addkey]) + '",\n')
                        else:
                            expectedlist.append(str(members[addkey]) + ',\n')
                for item in members['localStorage']['controllers']:
                        if 'logicalDrives' in item:
                            print "drivenumber is found"
                            if item['logicalDrives']:
                                for data in item['logicalDrives']:
                                    if 'driveNumber' in data:
                                        data.pop('driveNumber')
                        else:
                            print "ITEM NAME", item
                for membersKey in membersKeys:
                    answerlist = ''
                    if membersKey in membersDict:
                        f.write(' ' * 8 + '"' + membersKey + '": ' + dataTypeToSym[membersDict[membersKey + '_type'] + '_begin'] + '\n')
                        answerlist += ' ' * 8 + '"' + membersKey + '": ' + dataTypeToSym[membersDict[membersKey + '_type'] + '_begin'] + '\n'
                        if membersDict[membersKey + '_type'] == 'modDictListOfDict':
                            # get the listed key from each index of list of dictionaries
                            for membersDictKey in membersDict[membersKey]:
                                print "membersDictKey", membersDictKey
                                # checking for level2 list of dict
                                if membersDictKey == 'manageSanStorage':
                                    print "Managesanstorage", membersDictKey
                                    if members[membersKey][membersDictKey] == 'False':
                                        print "NO SAN STORAGE"
                                        continue
                                if membersDictKey in membersDict:
                                    f.write(' ' * 12 + '"' + membersDictKey + '": ' + dataTypeToSym[membersDict[membersDictKey + '_type'] + '_begin'] + '\n')
                                    answerlist += ' ' * 12 + '"' + membersDictKey + '": ' + dataTypeToSym[membersDict[membersDictKey + '_type'] + '_begin'] + '\n'
                                    if membersDict.get(membersDictKey + '_type') == 'listOfDict':
                                        beginFlag = 1
                                        for level2Value in members[membersKey][membersDictKey]:
                                            if 'boot' in level2Value and 'bootVolumeSource' in level2Value['boot']:
                                                if level2Value['boot']['bootVolumeSource'] == 'ManagedVolume':
                                                    bootflag = 0
                                                    print "primary boot found", level2Value['boot']
                                                    if 'targets' in level2Value['boot']:
                                                        level2Value['boot'].pop('targets')
                                            if beginFlag == 1:
                                                f.write(' ' * 16 + '{\n')
                                                answerlist += ' ' * 16 + '{\n'
                                            tmpList = []
                                            # loop thru list of dict
                                            for pos, level2Key in enumerate(membersDict[membersDictKey]):
                                                print "level2Key", level2Key
                                                if level2Key not in level2Value:
                                                    print "I AM HERE", level2Key
                                                    continue
                                                # this is where the likes of permittedInterconnectTypeUri will be processed
                                                if re.search('Uri$', level2Key):
                                                    # string uri
                                                    uriName = str(None)
                                                    if level2Value[level2Key] is not None:
                                                        uriName = resourceTools.add_tagname_to_uri(ip, sessionId, level2Value[level2Key], api=apiVersion)
                                                    uriName = self._ascii_encode(uriName)
                                                    f.write(' ' * 20 + '"' + level2Key + '": ' + str(uriName) + ',\n')
                                                    answerlist += ' ' * 20 + '"' + level2Key + '": ' + str(uriName) + ',\n'
                                                # check with membersDict if something was defined
                                                elif level2Key in membersDict and level2Key != 'boot':
                                                    f.write(' ' * 20 + '"' + level2Key + '": ' + dataTypeToSym[membersDict[level2Key + '_type'] + '_begin'] + '\n')
                                                    answerlist += ' ' * 20 + '"' + level2Key + '": ' + dataTypeToSym[membersDict[level2Key + '_type'] + '_begin'] + '\n'
                                                    # New code added Navya
                                                    if membersDict[level2Key + '_type'] == 'listOfDict':
                                                        # loop thru logicalLocation key value (dict)
                                                        for level3Value in level2Value[level2Key]:
                                                            f.write(' ' * 24 + '{\n')
                                                            answerlist += ' ' * 24 + '{\n'
                                                            # loop thru level3Value (dictionary value)
                                                            for level3Key in membersDict[level2Key]:
                                                                if level3Key == 'targets':
                                                                    level3Value[level3Key] = []
                                                                else:
                                                                    level3Value[level3Key] = self._ascii_encode(level3Value[level3Key])
                                                                f.write(' ' * 28 + '"' + level3Key + '": ' + str(level3Value[level3Key]))
                                                                f.write(',\n')
                                                                answerlist += ' ' * 28 + '"' + level3Key + '": ' + str(level3Value[level3Key]) + ',\n'
                                                            f.write(' ' * 24 + dataTypeToSym[membersDict[membersKey + '_type'] + '_end'] + ',\n')
                                                            answerlist += ' ' * 24 + dataTypeToSym[membersDict[membersKey + '_type'] + '_end'] + ',\n'
                                                    f.write('\n')
                                                    answerlist += '\n'
                                                    f.write(' ' * 20 + dataTypeToSym[membersDict[level2Key + '_type'] + '_end'] + ',\n')
                                                    answerlist += ' ' * 20 + dataTypeToSym[membersDict[level2Key + '_type'] + '_end'] + ',\n'
                                                else:
                                                    # immediate key-value pair here (no complicated data types)
                                                    print "level2Value[level2Key]", level2Key, level2Value[level2Key]
                                                    level2Value[level2Key] = self._ascii_encode(level2Value[level2Key])
                                                    if level2Value[level2Key] is not None:
                                                        f.write(' ' * 20 + '"' + level2Key + '": ' + str(level2Value[level2Key]) + ',\n')
                                                        answerlist += ' ' * 20 + '"' + level2Key + '": ' + str(level2Value[level2Key]) + ',\n'
                                                    else:
                                                        f.write(' ' * 20 + '"' + level2Key + '": ' + None + ',\n')
                                                        answerlist += ' ' * 20 + '"' + level2Key + '": ' + None + ',\n'
                                                # check with membersDict if something was defined
                                            f.write(' ' * 16 + '},\n')
                                            answerlist += ' ' * 16 + '},\n'
                                            if any('"type": "None"\n' == k for k in tmpList if k):
                                                beginFlag = 0
                                                continue
                                            else:
                                                beginFlag = 1
                                            [f.write(' ' * 16 + k) for k in tmpList if k]
                                    f.write(' ' * 12 + dataTypeToSym[membersDict[membersDictKey + '_type'] + '_end'] + '\n')
                                    answerlist += ' ' * 12 + dataTypeToSym[membersDict[membersDictKey + '_type'] + '_end'] + '\n'
                                else:
                                    # immediate second-level stuff
                                    print "not in membersdict", membersDictKey
                                    if membersDictKey not in members[membersKey]:
                                        print "Not in API output"
                                    else:
                                        members[membersKey][membersDictKey] = self._ascii_encode(members[membersKey][membersDictKey])
                                        f.write(' ' * 12 + '"' + membersDictKey + '": ' + str(members[membersKey][membersDictKey]))
                                        answerlist += ' ' * 12 + '"' + membersDictKey + '": ' + str(members[membersKey][membersDictKey])
                                if membersDictKey in members[membersKey]:
                                    self._close_data(f, membersDictKey, membersDict[membersKey][-1], 0)
                                    answerlist += self._spaceformat_data(membersDictKey, membersDict[membersKey][-1], 0)
                        else:
                            # anything else outside type listOfDict
                            for membersDictKey in membersDict[membersKey]:
                                # grab whatever listed membersDict[membersKey]
                                if members[membersKey] is None:
                                    print "There is no data for key", membersKey
                                    continue
                                members[membersKey][membersDictKey] = self._ascii_encode(members[membersKey][membersDictKey])
                                f.write(' ' * 12 + '"' + membersDictKey + '": ')
                                f.write(str(members[membersKey][membersDictKey]))
                                self._close_data(f, membersDictKey, membersDict[membersKey][-1], 0)
                                answerlist += ' ' * 12 + '"' + membersDictKey + '": '
                                answerlist += str(members[membersKey][membersDictKey])
                                answerlist += self._spaceformat_data(membersDictKey, membersDict[membersKey][-1], 0)
                        f.write(' ' * 8 + dataTypeToSym[membersDict[membersKey + '_type'] + '_end'] + ',\n')
                        answerlist += ' ' * 8 + dataTypeToSym[membersDict[membersKey + '_type'] + '_end'] + ',\n'
                    elif isinstance(membersKey, dict):
                        f.write(' ' * 8 + '"' + membersKey + '": ' + dataTypeToSym[membersDict[membersDictKey + '_type'] + '_begin'] + '\n')
                        answerlist += ' ' * 8 + '"' + membersKey + '": ' + dataTypeToSym[membersDict[membersDictKey + '_type'] + '_begin'] + '\n'
                        for memberKey in membersKey:
                            f.write(' ' * 8 + '"' + memberKey + '": ' + str(self._ascii_encode(members[membersKey][memberKey])))
                            answerlist += ' ' * 8 + '"' + memberKey + '": ' + str(self._ascii_encode(members[membersKey][memberKey]))
                        f.write(' ' * 8 + dataTypeToSym[membersDict[membersDictKey + '_type'] + '_end'] + '\n')
                        answerlist += ' ' * 8 + dataTypeToSym[membersDict[membersDictKey + '_type'] + '_end'] + '\n'
                    else:
                        print "membersKey in else", membersKey
                        if re.search('Uri$', membersKey):
                            uriName = str(None)
                            if membersKey == 'serverHardwareTypeUri':
                                print "I FOUND serverHardwareTypeUri"
                                uriName = resourceTools.get_mezz_model_by_shtname(ip, sessionId, members[membersKey], api=apiVersion)
                                answerlist += ' ' * 8 + '"' + membersKey + '": "' + str(uriName) + '"'
                            else:
                                if members[membersKey] is not None:
                                    uriName = resourceTools.add_tagname_to_uri(ip, sessionId, members[membersKey], api=apiVersion)
                                answerlist += ' ' * 8 + '"' + membersKey + '": "' + str(uriName) + '"'
                            f.write(' ' * 8 + '"' + membersKey + '": "' + str(uriName) + '"')
                        # check for conditional keys (global)
                        elif globalNegativeCondDict.get(membersKey) is not None and globalNegativeCondDict.get(membersKey) != members[membersKey] and globalNegativeCondDict.get(membersKey + '_' + members[membersKey]) is not None:
                            for k in globalNegativeCondDict.get(membersKey + '_' + members[membersKey]):
                                members[k] = self._ascii_encode(members[k])
                                f.write(' ' * 8 + '"' + k + '": ' + str(members[k]) + ',\n')
                                answerlist += ' ' * 8 + '"' + k + '": ' + str(members[k]) + ',\n'
                            members[membersKey] = self._ascii_encode(members[membersKey])
                            f.write(' ' * 8 + '"' + membersKey + '": ' + str(members[membersKey]))
                            answerlist += ' ' * 8 + '"' + membersKey + '": ' + str(members[membersKey])
                        else:
                            print "membersKey in URi else", membersKey
                            if membersKey not in members:
                                continue
                            if CIFIT_TYPE_CONV is True and membersKey == 'serialNumberType' and members[membersKey] == 'Virtual':
                                members[membersKey] = 'Virtual'
                            members[membersKey] = self._ascii_encode(members[membersKey])
                            f.write(' ' * 8 + '"' + membersKey + '": ' + str(members[membersKey]))
                            answerlist += ' ' * 8 + '"' + membersKey + '": ' + str(members[membersKey])
                        self._close_data(f, membersKey, membersKeys[-1], 0)
                        answerlist += self._spaceformat_data(membersKey, membersKeys[-1], 0)
                    expectedlist.append(answerlist)
                self._close_data(f, members, resourceData['members'][-1], 4, lineEnder='}')
                expectedlist.append(self._spaceformat_data(members, resourceData['members'][-1], 4, lineEnder='}'))
            f.write(']\n')
            f.close()
            expectedVarName = "expected_" + variableName
            self._write_data(fileName, expectedVarName, expectedlist)

    def rist_generate_storage_systems_variable_file(self, ip, sessionId, resourceData, fileName, variableName, vMapFile='../resources/config-files/storage-systems.conf', mode='append', apiVersion=None):
        """ storage system parser for variable file
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
            'expectedKeys': vConfig.expectedKeys,
            'deviceSpecificAttributesKeys': vConfig.deviceSpecificAttributesKeys,
            'membersDict': vConfig.membersDict,
            'keepUris': vConfig.keepUris,
            'globalNegativeCondDict': vConfig.globalNegativeCondDict,
            'nonglobalNegativeCondDict': vConfig.nonglobalNegativeCondDict
        }
        self.rist_create_variable_file_header(fileName, mode)
        resourceTools = RistConnections()
        expectedlist = []
        all_creds = data_variables.get_variables()
        print "STORAGE CREDENTAILs", all_creds['storage_credentials']
        virtualStoreName = None
        with open(fileName, 'a') as f:
            f.write(variableName + ' = [\n')
            for members in resourceData['members']:
                f.write(' ' * 4 + '{\n')
                expectedlist.append(' ' * 4 + '{\n')
                f.write(' ' * 8 + '"' + 'credentials' + '": ')
                actualdata = members['credentials']
                for cred in all_creds['storage_credentials']:
                    print "members hostname", members['hostname']
                    if members['hostname'] == cred['hostname']:
                        print "this is hostname matched"
                        actualdata['password'] = cred['password']
                f.write(str(actualdata) + ',\n')
                if members['family'] == 'StoreVirtual':
                    virtualStoreName = members['name']
                    print "System has Virtual Storage and has no devicespecificattributes", vKeys['membersKeys']
                    vKeys['membersKeys'] = self.criteria_filtering(vKeys['membersKeys'], ['deviceSpecificAttributes'])
                    print "After filtering", vKeys['membersKeys']
                elif members['family'] == 'StoreServ':
                    print "System has physical Storage and remove ports", vKeys['membersKeys']
                    if 'deviceSpecificAttributes' in vKeys['membersKeys']:
                        print "deviceSpecificAttributes key already present in list"
                    else:
                        vKeys['membersKeys'].append('deviceSpecificAttributes')
                    vKeys['membersKeys'] = self.criteria_filtering(vKeys['membersKeys'], ['ports'])
                    print "After filtering", vKeys['membersKeys']
                elif members['family'] == 'Nimble':
                    if 'ports' in vKeys['membersKeys']:
                        print "ports key already present in list"
                    else:
                        vKeys['membersKeys'].append('ports')
                    vKeys['membersKeys'] = self.criteria_filtering(
                        vKeys['membersKeys'], ['deviceSpecificAttributes'])
                    print "After filtering", vKeys['membersKeys']
                else:
                    pass
                for addkey in vKeys['expectedKeys']:
                    expectedlist.append(' ' * 8 + '"' + addkey + '": ')
                    if members[addkey] is not None:
                        if re.search('Uri$', addkey) or re.search('uri$', addkey):
                            nameuri = resourceTools.add_tagname_to_uri(ip, sessionId, members[addkey], api=apiVersion)
                            if nameuri is not None:
                                expectedlist.append('"' + str(nameuri) + '",\n')
                        else:
                            if str(members[addkey]).isdigit() or '[' in members[addkey]:
                                expectedlist.append(str(members[addkey]) + ',\n')
                            else:
                                expectedlist.append('"' + str(members[addkey]) + '",\n')
                    else:
                        expectedlist.append(str(members[addkey]) + ',\n')
                for membersKey in vKeys['membersKeys']:
                    answerlist = ''
                    if membersKey not in vKeys['membersDict']:
                        members[membersKey] = self._ascii_encode(members[membersKey])
                        f.write(' ' * 8 + '"' + membersKey + '": ' + str(members[membersKey]))
                        self._close_data(f, membersKey, vKeys['membersKeys'][-1], 0)
                        answerlist += ' ' * 8 + '"' + membersKey + '": ' + str(members[membersKey])
                        answerlist += self._spaceformat_data(membersKey, vKeys['membersKeys'][-1], 0)
                    elif vKeys['membersDict'][membersKey + '_type'] == 'dictionary':
                        f.write(' ' * 8 + '"' + membersKey + '": {\n')
                        answerlist += ' ' * 8 + '"' + membersKey + '": {\n'
                        for memberKey in vKeys['membersDict'][membersKey]:
                            if memberKey == "managedPools" or memberKey == "discoveredPools":
                                print "calling storage pool function", memberKey
                                poollist = self.rist_generate_storage_pools_state_variable_file(ip, sessionId, virtualStoreName, members['uri'], vMapFile='../resources/config-files/storage-pools_state.conf', apiVersion=apiVersion)
                                if memberKey == "managedPools":
                                    memberValue = poollist[0]
                                if memberKey == "discoveredPools":
                                    memberValue = poollist[1]
                            else:
                                memberValue = self._ascii_encode(members[membersKey][memberKey])
                            if memberKey == 'serialNumber':
                                if memberKey in answerlist and memberValue in answerlist:
                                    answerlist += ' ' * 12 + '"' + memberKey + '": ' + str(memberValue)
                            else:
                                f.write(' ' * 12 + '"' + memberKey + '": ' + str(memberValue))
                            self._close_data(f, memberKey, vKeys['membersDict'][membersKey][-1], 0)
                            if memberKey not in ["managedPools", "discoveredPools"]:
                                answerlist += ' ' * 12 + '"' + memberKey + '": ' + str(memberValue)
                                answerlist += self._spaceformat_data(memberKey, vKeys['membersDict'][membersKey][-1], 0)
                        self._close_data(f, members, resourceData['members'][-1], 8, lineEnder='}')
                        answerlist += self._spaceformat_data(members, resourceData['members'][-1], 8, lineEnder='}')
                    # Navya new elif for ports
                    elif vKeys['membersDict'][membersKey + '_type'] == 'listOfDict':
                        f.write(' ' * 8 + '"' + membersKey + '": [\n')
                        answerlist += ' ' * 8 + '"' + membersKey + '": [\n'
                        for membersInDict in members[membersKey]:
                            f.write(' ' * 12 + '{\n')
                            answerlist += ' ' * 12 + '{\n'
                            # get the data from the keys listed in the likes of connections(in connectionsKeys)
                            for membersList in vKeys['membersDict'][membersKey]:
                                if membersList in membersInDict:
                                    f.write(' ' * 16 + '"' + membersList + '": ')
                                    answerlist += ' ' * 16 + '"' + membersList + '": '
                                    memberData = self._ascii_encode(membersInDict[membersList])
                                    if re.search('Uri$', membersList) or re.search('uri$', membersList):
                                        nameuri = resourceTools.add_tagname_to_uri(ip, sessionId, membersInDict[membersList], api=apiVersion)
                                        f.write('"' + str(nameuri) + '"')
                                        answerlist += '"' + str(nameuri) + '"'
                                    else:
                                        f.write(str(memberData))
                                        answerlist += str(memberData)
                                self._close_data(f, membersList, vKeys['membersDict'][membersKey][-1], 0)
                                answerlist += self._spaceformat_data(membersList, vKeys['membersDict'][membersKey][-1], 0)
                            self._close_data(f, membersInDict, members[membersKey][-1], 12, lineEnder='}')
                            answerlist += self._spaceformat_data(membersInDict, members[membersKey][-1], 12, lineEnder='}')
                        self._close_data(f, membersKey, vKeys['membersKeys'][-1], 8, lineEnder=']')
                        answerlist += self._spaceformat_data(membersKey, vKeys['membersKeys'][-1], 8, lineEnder=']')
                    expectedlist.append(answerlist)
                self._close_data(f, members, resourceData['members'][-1], 4, lineEnder='}')
                expectedlist.append(self._spaceformat_data(members, resourceData['members'][-1], 4, lineEnder='}'))
            f.write(']\n')
            f.close()
            expectedVarName = "expected_" + variableName
            self._write_data(fileName, expectedVarName, expectedlist)

    def rist_generate_storage_pools_state_variable_file(self, ip, sessionId, virtualStoreName, StorageUri, vMapFile='../resources/config-files/storage-pools_state.conf', apiVersion=None):
        """ storage pools parser for variable file
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
            'membersDict': vConfig.membersDict
        }
        managedPools = []
        discoveredPools = []
        resourceTools = RistConnections()
        resourceData = resourceTools.get_storage_pools(ip, sessionId, '/rest/storage-pools', api=apiVersion)
        print " I am inside Storage_pool function"
        for members in resourceData['members']:
            if StorageUri == members['storageSystemUri']:
                print "ON SAME STORAGE SYSTEM"
                storageName = resourceTools.get_attr_by_uri(ip, sessionId, members['storageSystemUri'], api=apiVersion)
                if storageName == virtualStoreName:
                    continue
                answerlist = {}
                for membersKey in vKeys['membersKeys']:
                    if isinstance(membersKey, unicode):
                        membersKey = unicodedata.normalize('NFKD', membersKey).encode('ascii', 'ignore')
                    if membersKey not in vKeys['membersDict']:
                        print "I AM IN NOT IN", membersKey
                        if isinstance(members[membersKey], unicode):
                            members[membersKey] = unicodedata.normalize('NFKD', members[membersKey]).encode('ascii', 'ignore')
                        answerlist[membersKey] = members[membersKey]
                    elif vKeys['membersDict'][membersKey + '_type'] == 'dictionary':
                        for memberKey in vKeys['membersDict'][membersKey]:
                            print "I AM IN FOR LOOP", memberKey
                            memberValue = self._ascii_encode(members[membersKey][memberKey])
                            if isinstance(members[membersKey][memberKey], unicode):
                                memberValue = unicodedata.normalize('NFKD', members[membersKey][memberKey]).encode('ascii', 'ignore')
                            if memberKey == 'supportedRAIDLevel':
                                memberKey = 'raidLevel'
                            if memberKey in answerlist:
                                answerlist[memberKey] += memberValue
                            else:
                                print "no key in answerlist"
                                answerlist[memberKey] = memberValue
                print "answerlist", answerlist
                if 'Managed' in answerlist['state']:
                    print "It is managedPools"
                    managedPools.append(answerlist)
                else:
                    print "it is DiscoveredPools"
                    discoveredPools.append(answerlist)
            else:
                print "Storage System does not match"
        print "managedpools", managedPools
        print "discoveredPOols", discoveredPools
        return [managedPools, discoveredPools]

    def rist_generate_storage_pools_variable_file(self, ip, sessionId, resourceData, fileName, variableName, vMapFile='../resources/config-files/storage-pools.conf', mode='append', apiVersion=None):
        """ storage pools parser for variable file
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
            'membersDict': vConfig.membersDict,
            'keepUris': vConfig.keepUris,
            'globalNegativeCondDict': vConfig.globalNegativeCondDict,
            'nonglobalNegativeCondDict': vConfig.nonglobalNegativeCondDict
        }
        expectedVariable = None
        self.variable_file_generic2_parser(ip, sessionId, resourceData, fileName, variableName, expectedVariable, vKeys, mode, apiVersion=apiVersion)

    def rist_generate_svt_variable_file(self, ip, sessionId, resourceData, fileName, variableName, vMapFile='../resources/config-files/storage-templates.conf', mode='append', apiVersion=None):
        """ storage volume templates parser for variable file
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

        vKeys = {
            'membersKeys': vConfig.membersKeys,
            'expectedKeys': vConfig.expectedKeys,
            'membersDict': vConfig.membersDict
        }

        self.rist_create_variable_file_header(fileName, mode)
        resourceTools = RistConnections()
        expectedlist = []
        with open(fileName, 'a') as f:
            f.write(variableName + ' = [\n')
            for members in resourceData['members']:
                f.write(' ' * 4 + '{\n')
                expectedlist.append(' ' * 4 + '{\n')
                for addkey in vKeys['expectedKeys']:
                    expectedlist.append(' ' * 8 + '"' + addkey + '": ')
                    if members[addkey] is not None:
                        if re.search('Uri$', addkey) or re.search('uri$', addkey):
                            nameuri = resourceTools.add_tagname_to_uri(ip, sessionId, members[addkey], api=apiVersion)
                            if nameuri is not None:
                                expectedlist.append('"' + str(nameuri) + '",\n')
                        else:
                            if str(members[addkey]).isdigit() or '[' in members[addkey]:
                                expectedlist.append(str(members[addkey]) + ',\n')
                            else:
                                expectedlist.append('"' + str(members[addkey]) + '",\n')
                    else:
                        expectedlist.append(str(members[addkey]) + ',\n')
                for membersKey in vKeys['membersKeys']:
                    answerlist = ''
                    if membersKey not in vKeys['membersDict']:
                        members[membersKey] = self._ascii_encode(members[membersKey])
                        f.write(' ' * 8 + '"' + membersKey + '": ' + str(members[membersKey]))
                        self._close_data(f, membersKey, vKeys['membersKeys'][-1], 0)
                        answerlist += ' ' * 8 + '"' + membersKey + '": ' + str(members[membersKey])
                        answerlist += self._spaceformat_data(membersKey, vKeys['membersKeys'][-1], 0)
                    elif vKeys['membersDict'][membersKey + '_type'] == 'dictOfDict':
                        f.write(' ' * 8 + '"' + membersKey + '": {\n')
                        answerlist += ' ' * 8 + '"' + membersKey + '": {\n'
                        for memberKey in vKeys['membersDict'][membersKey]:
                            if memberKey not in members[membersKey]:
                                print "There is no Snapshot pool"
                                continue
                            f.write(' ' * 12 + '"' + memberKey + '": {\n')
                            answerlist += ' ' * 12 + '"' + memberKey + '": {\n'
                            for level2Key in members[membersKey][memberKey]:
                                if isinstance(members[membersKey][memberKey][level2Key], dict):
                                    f.write(' ' * 16 + '"' + level2Key + '": {\n')
                                    answerlist += ' ' * 16 + '"' + level2Key + '": {\n'
                                    for level3Key in members[membersKey][memberKey][level2Key]:
                                        level3KeyVal = self._ascii_encode(members[membersKey][memberKey][level2Key][level3Key])
                                        f.write(' ' * 20 + '"' + level3Key + '": ' + level3KeyVal + ',\n')
                                        answerlist += ' ' * 20 + '"' + level3Key + '": ' + level3KeyVal + ',\n'
                                    f.write(' ' * 16 + '}')
                                    answerlist += ' ' * 16 + '}'
                                elif (memberKey == 'storagePool' or memberKey == 'snapshotPool') and str(level2Key) == 'default':
                                    uriName = resourceTools.get_attr_by_uri(ip, sessionId, members[membersKey][memberKey][level2Key], api=apiVersion)
                                    f.write(' ' * 16 + '"' + str(level2Key) + '": "' + str(uriName) + '"')
                                    answerlist += ' ' * 16 + '"' + str(level2Key) + '": "SPOOL:' + str(uriName) + '"'
                                else:
                                    memberValue = self._ascii_encode(members[membersKey][memberKey][level2Key])
                                    f.write(' ' * 16 + '"' + level2Key + '": ' + memberValue)
                                    answerlist += ' ' * 16 + '"' + level2Key + '": ' + memberValue
                                self._close_data(f, memberKey, members[membersKey][memberKey].keys()[-1], 0)
                                answerlist += self._spaceformat_data(memberKey, members[membersKey][memberKey].keys()[-1], 0)
                            self._close_data(f, members, vKeys['membersDict'][membersKey][-1], 12, lineEnder='}')
                            answerlist += self._spaceformat_data(members, vKeys['membersDict'][membersKey][-1], 12, lineEnder='}')
                        self._close_data(f, members, resourceData['members'][-1], 8, lineEnder='}')
                        answerlist += self._spaceformat_data(members, resourceData['members'][-1], 8, lineEnder='}')
                    expectedlist.append(answerlist)
                self._close_data(f, members, resourceData['members'][-1], 4, lineEnder='}')
                expectedlist.append(self._spaceformat_data(members, resourceData['members'][-1], 4, lineEnder='}'))
            f.write(']\n')
            f.close()
            print "EXPECTEDLIST", expectedlist
            expectedVarName = "expected_" + variableName
            self._write_data(fileName, expectedVarName, expectedlist)

    def rist_separate_new_existing_volumes_variable(self, ip, sessionId, resourceData, fileName, variableName, vMapFile='../resources/config-files/storage-volumes.conf', mode='append', apiVersion=None):
        existing_volumes = []
        new_volumes = []
        existing_volumes_dict = {}
        new_volumes_dict = {}
        matchstring = 'Existing_Volume'
        pattern = r'\bExisting_Volume\b'
        for members in resourceData['members']:
            if 'description' in members:
                print "description is found", members['description']
                matchobject = re.search(pattern, members['description'], re.I)
                if matchobject:
                    print "It is Pre-Existing Volume", matchobject.group(0)
                    existing_volumes.append(members)
                else:
                    print "New Volumes"
                    new_volumes.append(members)
        existing_volumes_dict['members'] = existing_volumes
        new_volumes_dict['members'] = new_volumes
        varName = 'add_existing_storage_volumes'
        self.rist_generate_existing_volumes_variable_file(ip, sessionId, existing_volumes_dict, fileName, varName, vMapFile='../resources/config-files/storage-volumes.conf', mode='append', apiVersion=apiVersion)
        self.rist_generate_storage_volumes_variable_file(ip, sessionId, new_volumes_dict, fileName, variableName, vMapFile='../resources/config-files/storage-volumes.conf', mode='append', apiVersion=apiVersion)

    def rist_generate_existing_volumes_variable_file(self, ip, sessionId, resourceData, fileName, variableName, vMapFile='../resources/config-files/storage-volumes.conf', mode='append', apiVersion=None):
        """ storage volumes parser for variable file
            [Arguments]
            ip - OV IP
            sessionId - OV session Id
            resourceData - dictionary of resource data
            fileName - file to save parsed data to
            variableName - name of variable to assign parsed data to
            vMapFile - [optional] resource's variable-to-keys mapping
            mode - [optional] write or append to fileName
        """

        print "apiVersion", apiVersion
        with open(vMapFile, 'r') as r:
            vConfig = imp.new_module('data')
            exec(r.read(), vConfig.__dict__)
        membersKeys = vConfig.membersKeys
        expectedKeys = vConfig.expectedKeys
        expectedlist = []
        self.rist_create_variable_file_header(fileName, mode)
        resourceTools = RistConnections()
        with open(fileName, 'a') as f:
            f.write(variableName + ' = [\n')
            for members in resourceData['members']:
                f.write(' ' * 4 + '{\n')
                expectedlist.append(' ' * 4 + '{\n')
                for addkey in expectedKeys:
                    expectedlist.append(' ' * 8 + '"' + addkey + '": ')
                    if members[addkey] is not None:
                        if re.search('Uri$', addkey) or re.search('uri$', addkey):
                            nameuri = resourceTools.add_tagname_to_uri(ip, sessionId, members[addkey], api=apiVersion)
                            if nameuri is not None:
                                expectedlist.append('"' + str(nameuri) + '",\n')
                        else:
                            if str(members[addkey]).isdigit() or '[' in members[addkey]:
                                expectedlist.append(str(members[addkey]) + ',\n')
                            else:
                                expectedlist.append('"' + str(members[addkey]) + '",\n')
                    else:
                        expectedlist.append(str(members[addkey]) + ',\n')
                if 'deviceVolumeName' in members:
                    f.write(' ' * 8 + '"' + 'deviceVolumeName' + '": ')
                    f.write('"' + str(members['deviceVolumeName']) + '",\n')
                    expectedlist.append(' ' * 8 + '"' + 'deviceVolumeName' + '": ')
                    expectedlist.append('"' + str(members['deviceVolumeName']) + '",\n')
                for memberKey in membersKeys:
                    answerlist = ''
                    if memberKey == 'storagePool':
                        if members['storagePoolUri'] is not None:
                            storageSystemUri = resourceTools.get_attr_by_uri(ip, sessionId, members['storagePoolUri'], attr='storageSystemUri', api=apiVersion)
                            print "storageSystemUri", storageSystemUri
                            if storageSystemUri is not None:
                                storageName = resourceTools.get_attr_by_uri(ip, sessionId, storageSystemUri, api=apiVersion)
                                print "storageName", storageName
                            f.write(' ' * 8 + '"' + 'storageSystemUri' + '": ')
                            f.write('"' + str(storageName) + '"')
                            answerlist += ' ' * 8 + '"' + 'storagePoolUri' + '": '
                            answerlist += '"SPOOL:' + str(resourceTools.get_attr_by_uri(ip, sessionId, members['storagePoolUri'], api=apiVersion)) + '"'
                        else:
                            storagePoolUri = str(None)
                            f.write(' ' * 8 + '"' + 'storageSystemUri' + '": ' + str(storagePoolUri))
                            answerlist += ' ' * 8 + '"' + 'storagePoolUri' + '": ' + str(storagePoolUri)
                    elif memberKey in ['isPermanent', 'provisioningType', 'size']:
                        continue
                    else:
                        memberValue = self._ascii_encode(members[memberKey])
                        f.write(' ' * 8 + '"' + memberKey + '": ' + memberValue)
                        answerlist += ' ' * 8 + '"' + memberKey + '": ' + memberValue
                    expectedlist.append(answerlist)
                    expectedlist.append(self._spaceformat_data(memberKey, membersKeys[-1], 0))
                    self._close_data(f, memberKey, membersKeys[-1], 0)
                # self._close_data(f, members, resourceData['members'][-1], 8, lineEnder='}')
                self._close_data(f, members, resourceData['members'][-1], 4, lineEnder='}')
                # expectedlist.append(self._spaceformat_data(members, resourceData['members'][-1], 8, lineEnder='}'))
                expectedlist.append(self._spaceformat_data(members, resourceData['members'][-1], 4, lineEnder='}'))
            f.write(']\n')
            f.close()
            print "EXPECTEDLIST", expectedlist
            expectedVarName = "expected_" + "existing_storage_volumes"
            self._write_data(fileName, expectedVarName, expectedlist)

    def rist_generate_storage_volumes_variable_file(self, ip, sessionId, resourceData, fileName, variableName, vMapFile='../resources/config-files/storage-volumes.conf', mode='append', apiVersion=None):
        """ storage volumes parser for variable file
            [Arguments]
            ip - OV IP
            sessionId - OV session Id
            resourceData - dictionary of resource data
            fileName - file to save parsed data to
            variableName - name of variable to assign parsed data to
            vMapFile - [optional] resource's variable-to-keys mapping
            mode - [optional] write or append to fileName
        """

        print "apiVersion", apiVersion
        with open(vMapFile, 'r') as r:
            vConfig = imp.new_module('data')
            exec(r.read(), vConfig.__dict__)
        membersKeys = vConfig.membersKeys

        expectedlist = []
        self.rist_create_variable_file_header(fileName, mode)
        resourceTools = RistConnections()
        with open(fileName, 'a') as f:
            f.write(variableName + ' = [\n')
            for members in resourceData['members']:
                f.write(' ' * 4 + '{\n')
                expectedlist.append(' ' * 4 + '{\n')
                if 'status' in members:
                    expectedlist.append(' ' * 8 + '"' + 'status' + '": ')
                    if members['status'] != 'None':
                        expectedlist.append('"' + str(members['status']) + '",\n')
                    else:
                        expectedlist.append(members['status'])
                if 'uri' in members:
                    nameuri = resourceTools.add_tagname_to_uri(ip, sessionId, members['uri'], api=apiVersion)
                    expectedlist.append(' ' * 8 + '"' + 'uri' + '": ')
                    expectedlist.append('"' + str(nameuri) + '"')
                    expectedlist.append(',\n')
                if members['volumeTemplateUri'] is not None:
                    templateUri = '"' + resourceTools.get_attr_by_uri(ip, sessionId, members['volumeTemplateUri'], api=apiVersion) + '"'
                    f.write(' ' * 8 + '"templateUri": ' + str(templateUri) + ',\n')
                else:
                    f.write(' ' * 8 + '"templateUri": "ROOT"' + ',\n')
                if 'isShareable' in members:
                    if members['isShareable']:
                        f.write(' ' * 8 + '"' + 'isPermanent' + '": ' + self._ascii_encode(members['isPermanent']) + ',\n')
                        expectedlist.append(' ' * 8 + '"' + 'isPermanent' + '": ' + self._ascii_encode(members['isPermanent']) + ',\n')
                f.write(' ' * 8 + '"properties": {\n')
                expectedlist.append(' ' * 8 + '"properties": {\n')
                for memberKey in membersKeys:
                    answerlist = ''
                    if memberKey == 'storagePool':
                        if members['storagePoolUri'] is not None:
                            storagePoolUri = resourceTools.get_attr_by_uri(ip, sessionId, members['storagePoolUri'], api=apiVersion)
                            f.write(' ' * 12 + '"' + memberKey + '": ')
                            f.write('"' + str(storagePoolUri) + '"')
                            answerlist += ' ' * 12 + '"' + 'storagePoolUri' + '": '
                            answerlist += '"SPOOL:' + str(storagePoolUri) + '"'
                        else:
                            storagePoolUri = str(None)
                            f.write(' ' * 12 + '"' + memberKey + '": ' + str(storagePoolUri))
                            answerlist += ' ' * 12 + '"' + 'storagePoolUri' + '": ' + str(storagePoolUri)
                    else:
                        if memberKey == 'size':
                            f.write(' ' * 12 + '"size": ' + members['provisionedCapacity'])
                            answerlist += ' ' * 12 + '"size": ' + members['provisionedCapacity']
                        else:
                            memberValue = self._ascii_encode(members[memberKey])
                            f.write(' ' * 12 + '"' + memberKey + '": ' + memberValue)
                            answerlist += ' ' * 12 + '"' + memberKey + '": ' + memberValue
                    expectedlist.append(answerlist)
                    expectedlist.append(self._spaceformat_data(memberKey, membersKeys[-1], 0))
                    self._close_data(f, memberKey, membersKeys[-1], 0)
                self._close_data(f, members, resourceData['members'][-1], 8, lineEnder='}')
                self._close_data(f, members, resourceData['members'][-1], 4, lineEnder='}')
                expectedlist.append(self._spaceformat_data(members, resourceData['members'][-1], 8, lineEnder='}'))
                expectedlist.append(self._spaceformat_data(members, resourceData['members'][-1], 4, lineEnder='}'))
            f.write(']\n')
            f.close()
            expectedVarName = "expected_" + variableName
            self._write_data(fileName, expectedVarName, expectedlist)

    def rist_set_variables_in_file(self, fileName, variableNames):
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

        resourceTools = RistConnections()
        responseNameList = []
        for rawUri in members[membersKey]:
            responseName = resourceTools.get_attr_by_uri(ip, sessionId, rawUri, api=api, headers=headers)
            responseNameList.append(responseName)
        return responseNameList

    def rist_create_variable_file_header(self, fileName, mode):
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
        admin_creds = data_variables.get_variables()
        fileModeHeader = {
            'write': '#!/usr/bin/env python\n\n' + 'admin_credentials =' + str(admin_creds['ADMIN_CREDENTIALS']),
            'append': '\n'
        }
        if mode not in fileMode:
            print 'Warning: Unsupported file access mode in %s.%s' % (__file__, 'rist_create_variable_file_header')
        with open(fileName, fileMode[mode]) as f:
            f.write(fileModeHeader[mode])

    def variable_file_generic_parser(self, ip, sessionId, resourceData, fileName, variableName, expectedVarName, jsonKeysList, expectedKeys=None, mode='append', apiVersion=None):
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

        self.rist_create_variable_file_header(fileName, mode)
        resourceTools = RistConnections()
        expectedlist = []
        credlist = data_variables.get_variables()
        pwdlist = credlist['users_credentials']
        with open(fileName, 'a') as f:
            f.write(variableName + ' = [\n')
            for members in resourceData['members']:
                expectedlist.append(' ' * 4 + '{\n')
                f.write(' ' * 4 + '{\n')
                if variableName == 'enclosures':
                    f.write(' ' * 8 + '"' + 'username' + '": ""' + ',\n')
                    f.write(' ' * 8 + '"' + 'password' + '": ""' + ',\n')
                    f.write(' ' * 8 + '"' + 'force' + '": ' + 'True' + ',\n')
                if 'enabled' in members:
                    expectedlist.append(' ' * 8 + '"' + 'enabled' + '": ')
                    expectedlist.append(str(members['enabled']))
                    expectedlist.append(',\n')
                if expectedKeys:
                    for addkey in expectedKeys:
                        expectedlist.append(' ' * 8 + '"' + addkey + '": ')
                        if members[addkey] is not None:
                            if re.search('Uri$', addkey, re.IGNORECASE) and addkey != 'subnetUri':
                                nameuri = resourceTools.add_tagname_to_uri(ip, sessionId, members[addkey], api=apiVersion)
                                expectedlist.append('"' + str(nameuri) + '",\n')
                            elif addkey == 'subnetUri':
                                expectedlist.append(str(None) + ',\n')
                            else:
                                expectedlist.append('"' + str(members[addkey]) + '",\n')
                        else:
                            expectedlist.append(str(members[addkey]) + ',\n')
                for key in jsonKeysList:
                    print 'key', key
                    answerlist = ''
                    if re.search('Uri$', key):
                        uriName = str(None)
                        if members[key] is not None:
                            uriName = resourceTools.add_tagname_to_uri(ip, sessionId, members[key], api=apiVersion)
                        # answerlist.append(' ' * 8 + '"' + key + '": ')
                        answerlist += ' ' * 8 + '"' + key + '": '
                        f.write(' ' * 8 + '"' + key + '": ')
                        # handle to get FCOENetworkUri
                        if key == 'managedSanUri':
                            if members[key] is not None:
                                uriName = resourceTools.get_attr_by_uri(ip, sessionId, members[key], api=apiVersion)
                                answerlist += '"FCSan:' + str(uriName) + '"'
                                f.write('"FCSan:' + str(uriName) + '"')
                        else:
                            answerlist += '"' + str(uriName) + '"'
                            f.write('"' + str(uriName) + '"')
                    else:
                        if key not in members:
                            continue
                        members[key] = self._ascii_encode(members[key])
                        if key == 'status':
                            if variableName == 'servers':
                                f.write(' ' * 8 + '"' + key + '": ')
                                if members[key] != 'None':
                                    f.write(str(members[key]))
                                else:
                                    f.write(members[key])
                            answerlist += ' ' * 8 + '"' + key + '": '
                            if members[key] != 'None':
                                answerlist += str(members[key])
                            else:
                                answerlist += members[key]
                        else:
                            if key == 'userName' and variableName == 'users':
                                data = filter(lambda userdata: '"' + userdata['userName'] + '"' == str(members[key]), pwdlist)
                                print "data", data, type(data)
                                f.write(' ' * 8 + '"password": ')
                                if len(data) > 0:
                                    f.write('"' + data[0]['password'] + '",\n')
                                else:
                                    f.write('"",\n')
                            if key == 'activeOaPreferredIP':
                                f.write(' ' * 8 + '"' + 'hostname' + '": ')
                                f.write(str(members[key]) + ',\n')
                                continue
                            if key == 'forceInstallFirmware':
                                f.write(' ' * 8 + '"' + key + '": ')
                                f.write(str(members[key]) + ',\n')
                                continue
                            if key == 'permissions':
                                if 'ScopeUri' in key:
                                    print "scopeuri is found", key[0]['ScopeUri']
                            f.write(' ' * 8 + '"' + key + '": ')
                            f.write(str(members[key]))
                            answerlist += ' ' * 8 + '"' + key + '": '
                            answerlist += str(members[key])
                    expectedlist.append(answerlist)
                    self._close_data(f, key, jsonKeysList[-1], 0)
                    expectedlist.append(self._spaceformat_data(key, jsonKeysList[-1], 0))
                expectedlist.append(self._spaceformat_data(members, resourceData['members'][-1], 4, lineEnder='}'))
                self._close_data(f, members, resourceData['members'][-1], 4, lineEnder='}')
            f.write(']\n')
            f.close()
            print "EXPECTEDLIST", expectedlist
            if expectedVarName is not None:
                self._write_data(fileName, expectedVarName, expectedlist)

    def _spaceformat_data(self, arrayElement, arrayLastElement, spacing, lineEnder=''):
        """ format data to file
        """
        if arrayElement is not arrayLastElement:
            return ' ' * spacing + lineEnder + ',\n'
        else:
            return ' ' * spacing + lineEnder + '\n'

    def _write_data(self, fileName, variableName, data):
        """ write expectedvariable data to file
        """
        with open(fileName, 'a+') as f:

            f.write(variableName + ' = [\n')
            f.writelines(data)
            f.write(']\n')
            f.close()

    def criteria_filtering(self, aList, matchingFilter):
        """ filter element from list
        """
        deletionIndexes = []
        i = 0
        for listLine in aList:
            for match in matchingFilter:
                print "this is match", match
                print "this is line", listLine
                if match in str(listLine):
                    deletionIndexes.append(i)
                    break
                else:
                    continue
            i += 1
        for number in reversed(deletionIndexes):
            aList.pop(number)
        return aList

    def variable_file_generic2_parser(self, ip, sessionId, resourceData, fileName, variableName, expectedVarName, vKeys, mode, CIFIT_TYPE_CONV=False, apiVersion=None):
        """ Generic2 parser. Used by profiles, EG
        """
        self.rist_create_variable_file_header(fileName, mode)
        resourceTools = RistConnections()
        expectedlist = []
        version = resourceTools.get_current_api_version(ip, sessionId, '/rest/version', api=apiVersion)
        print "version", version
        version = int(version)
        with open(fileName, 'a') as f:
            f.write(variableName + ' = [\n')
            for members in resourceData['members']:
                expectedlist.append(' ' * 4 + '{\n')
                f.write(' ' * 4 + '{\n')
                if 'expectedKeys' in vKeys:
                    for addkey in vKeys['expectedKeys']:
                        print "addkey", addkey
                        expectedlist.append(' ' * 8 + '"' + addkey + '": ')
                        print "addkey value", members[addkey]
                        if members[addkey] is not None:
                            if re.search('Uri$', addkey) or re.search('uri$', addkey):
                                nameuri = resourceTools.add_tagname_to_uri(ip, sessionId, members[addkey], api=apiVersion)
                                if nameuri is not None:
                                    expectedlist.append('"' + str(nameuri) + '",\n')
                            else:
                                if addkey == 'associatedLogicalInterconnectGroups':
                                    urilist = [resourceTools.add_tagname_to_uri(ip, sessionId, key, api=apiVersion) for key in members[addkey]]
                                    expectedlist.append(str(urilist) + ',\n')
                                else:
                                    print "NOT LIG", addkey
                                    if str(members[addkey]).isdigit() or '[' in str(members[addkey]) or isinstance(str(members[addkey]), int):
                                        expectedlist.append(str(members[addkey]) + ',\n')
                                    else:
                                        expectedlist.append('"' + str(members[addkey]) + '",\n')
                        else:
                            expectedlist.append(str(members[addkey]) + ',\n')
                if variableName == 'server_profiles':
                    for item in members['localStorage']['controllers']:
                        if 'logicalDrives' in item:
                            map(lambda d: d.pop('driveNumber'), item['logicalDrives'])
                        else:
                            print "ITEM NAME", item
                print "apiVersion", apiVersion
                if version > 500 and variableName == 'encgroups_add':
                    print "Higher Version is installed and remove type in EG"
                    expectedlist.append(' ' * 8 + '"' + 'name' + '": ')
                    expectedlist.append('"' + str(members['name']) + '"' + ',\n')
                    expectedlist.append(' ' * 8 + '"' + 'type' + '": ')
                    expectedlist.append('"' + str(members['type']) + '"' + ',\n')
                    expectedlist.append(' ' * 8 + '"' + 'enclosureTypeUri' + '": ')
                    expectedlist.append('"' + str(members['enclosureTypeUri']) + '"' + ',\n')
                    expectedlist.append(' ' * 8 + '"' + 'stackingMode' + '": ')
                    expectedlist.append('"' + str(members['stackingMode']) + '"' + ',\n')
                    if 'ipAddressingMode' in members and members['ipAddressingMode'] == 'IpPool':
                        vKeys['membersKeys'].append('ipRangeUris')
                    else:
                        vKeys['membersKeys'] = self.criteria_filtering(vKeys['membersKeys'], ['ipRangeUris'])
                    if members['osDeploymentSettings']:
                        if 'manageOSDeployment' in members['osDeploymentSettings']:
                            if members['osDeploymentSettings']['manageOSDeployment']:
                                vKeys['membersKeys'].append('osDeploymentSettings')
                            else:
                                vKeys['membersKeys'] = self.criteria_filtering(vKeys['membersKeys'], ['osDeploymentSettings'])
                    vKeys['membersKeys'] = self.criteria_filtering(vKeys['membersKeys'], ['type', 'enclosureTypeUri', 'stackingMode'])
                for membersKey in vKeys['membersKeys']:
                    answerlist = ''
                    if membersKey not in vKeys['membersDict']:
                        # not a list of dict
                        if membersKey == 'providerDisplayName':
                            if members[membersKey] == 'Direct attach':
                                print "It is Direct attach SAN Manager"
                                pass
                            else:
                                print "displayname is found"
                                displaydata = members[membersKey]
                                continue
                        print "membersKey", membersKey
                        if membersKey in ['status', 'interconnectBayMappingCount']:
                            answerlist += ' ' * 8 + '"' + membersKey + '": '
                            if membersKey == 'status':
                                if members[membersKey] != 'None':
                                    answerlist += '"' + str(members[membersKey]) + '",\n'
                                else:
                                    answerlist += members[membersKey] + ',\n'
                            else:
                                answerlist += '"' + str(members[membersKey]) + '",\n'
                        else:
                            if re.search('Uri$', membersKey) and not any(membersKey == x for x in vKeys['keepUris'] if x):
                                uriName = str(None)
                                if members[membersKey] is not None:
                                    if 'storage_pools_toedit' in variableName:
                                        uriName = resourceTools.get_attr_by_uri(ip, sessionId, members[membersKey], api=apiVersion)
                                    else:
                                        uriName = resourceTools.add_tagname_to_uri(ip, sessionId, members[membersKey], api=apiVersion)
                                f.write(' ' * 8 + '"' + membersKey + '": ')
                                f.write('"' + str(uriName) + '"')
                                answerlist += ' ' * 8 + '"' + membersKey + '": '
                                if 'encgroups_add' in variableName:
                                    answerlist += '"' + members[membersKey] + '"'
                                else:
                                    answerlist += '"' + str(uriName) + '"'
                            # check for conditional keys (global)
                            elif vKeys['globalNegativeCondDict'].get(membersKey) is not None and vKeys['globalNegativeCondDict'].get(membersKey) != members[membersKey] and vKeys['globalNegativeCondDict'].get(membersKey + '_' + members[membersKey]) is not None:
                                for k in vKeys['globalNegativeCondDict'].get(membersKey + '_' + members[membersKey]):
                                    members[k] = self._ascii_encode(members[k])
                                    f.write(' ' * 8 + '"' + k + '": ' + str(members[k]) + ',\n')
                                    answerlist += ' ' * 8 + '"' + k + '": ' + str(members[k]) + ',\n'
                                members[membersKey] = self._ascii_encode(members[membersKey])
                                f.write(' ' * 8 + '"' + membersKey + '": ' + str(members[membersKey]))
                                answerlist += ' ' * 8 + '"' + membersKey + '": ' + str(members[membersKey])
                            else:
                                if membersKey not in members:
                                    continue
                                if CIFIT_TYPE_CONV is True and membersKey == 'serialNumberType' and members[membersKey] == 'Virtual':
                                    members[membersKey] = 'Virtual'
                                members[membersKey] = self._ascii_encode(members[membersKey])
                                f.write(' ' * 8 + '"' + membersKey + '": ' + str(members[membersKey]))
                                answerlist += ' ' * 8 + '"' + membersKey + '": ' + str(members[membersKey])
                            self._close_data(f, membersKey, vKeys['membersKeys'][-1], 0)
                            answerlist += self._spaceformat_data(membersKey, vKeys['membersKeys'][-1], 0)
                    elif vKeys['membersDict'][membersKey + '_type'] == 'listOfDict':
                        # build the list of dictionary
                        if len(members[membersKey]) == 0:
                            continue
                        f.write(' ' * 8 + '"' + membersKey + '": [\n')
                        answerlist += ' ' * 8 + '"' + membersKey + '": [\n'
                        if variableName == 'san_managers':
                            f.write(' ' * 12 + '{\n')
                            f.write(' ' * 16 + '"' + vKeys['membersDict'][membersKey][0] + '": ')
                            f.write("'" + 'type' + "',\n")
                            f.write(' ' * 16 + '"' + vKeys['membersDict'][membersKey][1] + '": ')
                            f.write("'" + str(displaydata) + "'," + '\n')
                            f.write(' ' * 12 + '},\n')
                        # loop thru that members list of dict (like connections list declared above)
                        for membersInDict in members[membersKey]:
                            f.write(' ' * 12 + '{\n')
                            answerlist += ' ' * 12 + '{\n'
                            # get the data from the keys listed in the likes of connections(in connectionsKeys)
                            for membersList in vKeys['membersDict'][membersKey]:
                                if re.search('Uri$', membersList) and not any(membersList == x for x in vKeys['keepUris'] if x):
                                    uriName = str(None)
                                    if membersInDict[membersList] is not None:
                                        uriName = resourceTools.add_tagname_to_uri(ip, sessionId, membersInDict[membersList], api=apiVersion)
                                    f.write(' ' * 16 + '"' + membersList + '": ')
                                    f.write('"' + str(uriName) + '"')
                                    answerlist += ' ' * 16 + '"' + membersList + '": '
                                    answerlist += '"' + str(uriName) + '"'
                                # check for conditional keys (non-global)
                                elif vKeys['nonglobalNegativeCondDict'].get(membersList) is not None and vKeys['nonglobalNegativeCondDict'].get(membersList) != membersInDict[membersList] and vKeys['nonglobalNegativeCondDict'].get(membersList + '_' + membersInDict[membersList]) is not None:
                                    for k in vKeys['nonglobalNegativeCondDict'].get(membersList + '_' + membersInDict[membersList]):
                                        membersInDict[k] = self._ascii_encode(membersInDict[k])
                                        f.write(' ' * 16 + '"' + k + '": ' + str(membersInDict[k]) + ',\n')
                                        answerlist += ' ' * 16 + '"' + k + '": ' + str(membersInDict[k]) + ',\n'
                                    f.write(' ' * 16 + '"' + membersList + '": ')
                                    answerlist += ' ' * 16 + '"' + membersList + '": '
                                    membersInDict[membersList] = self._ascii_encode(membersInDict[membersList])
                                    f.write(str(membersInDict[membersList]))
                                    answerlist += str(membersInDict[membersList])
                                else:
                                    print "membersList", membersList, membersInDict
                                    if membersList in membersInDict:
                                        if CIFIT_TYPE_CONV is True and membersList == 'macType' and membersInDict[membersList] == 'Virtual':
                                                membersInDict[membersList] = 'UserDefined'
                                        membersInDict[membersList] = self._ascii_encode(membersInDict[membersList])
                                        if membersList == 'enclosureIndex':
                                            f.write(' ' * 16 + '"' + membersList + '": ')
                                            f.write(str(membersInDict[membersList]))
                                        else:
                                            f.write(' ' * 16 + '"' + membersList + '": ')
                                            answerlist += ' ' * 16 + '"' + membersList + '": '
                                            f.write(str(membersInDict[membersList]))
                                            answerlist += str(membersInDict[membersList])
                                self._close_data(f, membersList, vKeys['membersDict'][membersKey][-1], 0)
                                answerlist += self._spaceformat_data(membersList, vKeys['membersDict'][membersKey][-1], 0)
                            self._close_data(f, membersInDict, members[membersKey][-1], 12, lineEnder='}')
                            answerlist += self._spaceformat_data(membersInDict, members[membersKey][-1], 12, lineEnder='}')
                        self._close_data(f, membersKey, vKeys['membersKeys'][-1], 8, lineEnder=']')
                        answerlist += self._spaceformat_data(membersKey, vKeys['membersKeys'][-1], 8, lineEnder=']')
                    # Add one more else
                    else:
                        if membersKey == 'status':
                            answerlist += ' ' * 8 + '"' + membersKey + '": '
                            if str(members[membersKey]):
                                answerlist += '"' + str(members[membersKey]) + '"'
                            else:
                                answerlist += str(members[membersKey])
                        if vKeys['membersDict'][membersKey + '_type'] == 'dictionary':
                            if members[membersKey] is None:
                                f.write(' ' * 8 + '"' + membersKey + '": None,\n')
                                answerlist += ' ' * 8 + '"' + membersKey + '": None,\n'
                            else:
                                f.write(' ' * 8 + '"' + membersKey + '": ' + '{' + '\n')
                                answerlist += ' ' * 8 + '"' + membersKey + '": ' + '{' + '\n'
                                for membersInDict in members[membersKey]:
                                    if members[membersKey][membersInDict] is not None:
                                        members[membersKey][membersInDict] = self._ascii_encode(members[membersKey][membersInDict])
                                        f.write(' ' * 12 + '"' + membersInDict + '": ')
                                        answerlist += ' ' * 12 + '"' + membersInDict + '": '
                                        if 'profiles' in variableName and membersInDict == 'order':
                                            orders = members[membersKey][membersInDict].strip('[]')
                                            orderlist = list(orders.split(','))
                                            f.write(str('[' + orderlist[0] + ']'))
                                            answerlist += str('[' + orderlist[0] + ']')
                                        else:
                                            f.write(str(members[membersKey][membersInDict]))
                                            answerlist += str(members[membersKey][membersInDict])
                                        self._close_data(f, membersInDict, members[membersKey].keys()[-1], 0)
                                        answerlist += self._spaceformat_data(membersInDict, members[membersKey].keys()[-1], 0)
                                    else:
                                        f.write(' ' * 12 + '"' + membersInDict + '": ')
                                        f.write("None")
                                        self._close_data(f, membersInDict, members[membersKey].keys()[-1], 0)
                                        answerlist += ' ' * 12 + '"' + membersInDict + '": '
                                        answerlist += "None"
                                        answerlist += self._spaceformat_data(membersInDict, members[membersKey].keys()[-1], 0)

                                f.write(' ' * 8 + '},' + '\n')
                                answerlist += ' ' * 8 + '},' + '\n'
                    expectedlist.append(answerlist)
                self._close_data(f, members, resourceData['members'][-1], 4, lineEnder='}')
                expectedlist.append(self._spaceformat_data(members, resourceData['members'][-1], 4, lineEnder='}'))
            f.write(']\n')
            f.close()
            print "EXPECTEDLIST", expectedlist
            if expectedVarName is not None:
                self._write_data(fileName, expectedVarName, expectedlist)

    def rist_annotate(self, gen):
        prev_key, prev_val = 0, gen.next()
        for k, v in enumerate(gen, start=1):
            yield prev_key, prev_val
            prev_key, prev_val = k, v
        yield '-1', prev_val

    def rist_deep_copy(self, srcObj):
        """ Robot Framework has a bug particularly in Copy Dictionary.
            It appear to create reference instead of a mutable one.
            Wrapping deep copy to get around this issue.
        """
        destObj = copy.deepcopy(srcObj)
        return destObj

    def rist_return_nonzero_count(self, dict1, dict2):
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
