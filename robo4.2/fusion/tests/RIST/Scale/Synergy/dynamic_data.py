class DynamicData(object):

    def _init_(self):
        # valid characters
        self.chars = [chr(x) for x in range(33, 127)]

    def rename_enclosure(self, enclosures):
        ret = []
        for enc in enclosures:
            ret.append({"op": "replace", "path": "/name", "value": enc['scaleName'], "name": enc['serialNumber']})
        return ret

    def expected_enclosure_data(self, enclosures):
        ret = []
        for enc in enclosures:
            ret.append({'name': enc['scaleName'], 'serialNumber': enc['serialNumber'], 'type': 'EnclosureV400'})
        return ret

    def get_spp_path(self, name, local_dir, ftp_site_dir):
        ftp_path = ftp_site_dir + name + '.iso'
        local_path = local_dir + name + '.iso'
        return ftp_path, local_path

    def expected_spp_data(self, name):
        ret = []
        ret.append({'type': 'firmware-baselines', 'name': name + '.iso'})
        return ret

    def users_data(self, users):
        user_data = []
        for user in users:
            user_data.append({'userName': user['name'], 'password': 'hpvse123', 'fullName': user['name'], 'roles': [user['role']],
                              'emailAddress': user['name'] + '@hpe.com', 'officePhone': '970-898-2222', 'mobilePhone': '970-898-0022', 'type': 'UserAndRoles'})
        return user_data

    def expected_users_data(self, users):
        expected_user_data = []
        for user in users:
            expected_user_data.append({'userName': user['name'], 'fullName': user['name'], 'roles': [user['role']],
                                       'emailAddress': user['name'] + '@hpe.com', 'officePhone': '970-898-2222', 'mobilePhone': '970-898-0022', 'type': 'UserAndRoles'})
        return expected_user_data

    def make_ad_dict(self, ads):
        ret = []
        for ad in ads:
            ret.append({'type': 'LoginDomainConfigVersion200', 'name': ad['name'], 'authProtocol': 'AD', 'orgUnits': [], 'userNamingAttribute': 'UID', 'baseDN': ad['baseDN'],
                        'credential': {'userName': ad['user'], 'password': ad['password']},
                        'directoryServers': [{'type': 'LoginDomainDirectoryServerInfoDto',
                                              'directoryServerSSLPortNumber': ad['directoryServerSSLPortNumber'],
                                              'directoryServerIpAddress': ad['directoryServerIpAddress'],
                                              'directoryServerCertificateStatus': '',
                                              'serverStatus': '',
                                              'directoryServerCertificateBase64Data': ad['directoryServerCertificateBase64Data']}]})
        return ret

#     def make_expected_lig_dataold(self, ligs):
#         ret = []
#         for lig in ligs:
#             for uplink_set in lig['uplinkSets']:
#                 if uplink_set['networkType'] == 'FibreChannel':
#                     networkUris = 'FC:' + str(uplink_set['networkUris'])
#                     uplink_set['networkUris'] = networkUris
#                 if uplink_set['networkType'] == 'Ethernet':
#                     networkUris = []
#                     for networkUri in uplink_set['networkUris']:
#                         network = 'ETH:' + str(networkUri)
#                         networkUris.append(network)
#                     uplink_set['networkUris'] = networkUris
#             ret.append({'name': lig['name'], 'type': 'logical-interconnect-groupV300', 'uplinkSets': lig['uplinkSets'],
#                         'interconnectBaySet': lig['interconnectBaySet'], 'redundancyType': lig['redundancyType'], 'enclosureIndexes': lig['enclosureIndexes']})
#         return ret

    def make_expected_lig_data(self, ligs):
        ret = []
        for lig in ligs:
            ret.append({'name': lig['name'], 'type': 'logical-interconnect-groupV300'})
        return ret

#     def make_expected_saslig_dataold(self, sasligs):
#         ret = []
#         for saslig in sasligs:
#             ret.append({'name': saslig['name'], 'type': 'sas-logical-interconnect-group',
#                         'interconnectBaySet': saslig['interconnectBaySet'], 'enclosureIndexes': saslig['enclosureIndexes']})
#         return ret

    def make_expected_saslig_data(self, sasligs):
        ret = []
        for saslig in sasligs:
            ret.append({'name': saslig['name'], 'type': 'sas-logical-interconnect-group'})
        return ret

    def make_enc_group_data(self, enc_grps):
        ret = []
        for enc_grp in enc_grps:
            interconnect = []
            for x in range(1, enc_grp['enclosureCount'] + 1):
                for interconnectBayMapping in enc_grp['interconnectBayMappings']:
                    interconnect.append({'enclosureIndex': x, 'interconnectBay': interconnectBayMapping['bay'], 'logicalInterconnectGroupUri': interconnectBayMapping['lig']})
            ret.append({'name': enc_grp['name'], 'type': 'EnclosureGroupV400', 'enclosureCount': enc_grp['enclosureCount'], 'stackingMode': 'Enclosure',
                        'interconnectBayMappings': interconnect, 'ipAddressingMode': enc_grp['ipAddressingMode'], 'powerMode': 'RedundantPowerFeed'})
        return ret

#     def make_expected_enc_group_dataold(self, enc_grps):
#         ret = []
#         for enc_grp in enc_grps:
#             interconnect = []
#             for i in range(1, 7):
#                 interconnect.append({'interconnectBay': i, 'logicalInterconnectGroupUri': enc_grp['interconnectBayMappings'][i - 1]['lig']})
#             ret.append({'name': enc_grp['name'], 'type': 'EnclosureGroupV400', 'enclosureCount': enc_grp['enclosureCount'], 'stackingMode': 'Enclosure',
#                         'ipAddressingMode': enc_grp['ipAddressingMode'], 'powerMode': 'RedundantPowerFeed'})
#         return ret

    def make_expected_enc_group_data(self, enc_grps):
        ret = []
        for enc_grp in enc_grps:
            ret.append({'name': enc_grp['name'], 'type': 'EnclosureGroupV400'})
        return ret

#     def make_expected_logical_enclosure_dataold(self, les):
#         ret = []
#         for le in les:
#             ret.append({'type': 'LogicalEnclosureV400', 'name': le['name'], 'status': 'OK',
#                         'enclosureUris': le['enclosureUris'], 'enclosureGroupUri': le['enclosureGroupUri']})
#         return ret

    def make_expected_logical_enclosure_data(self, les):
        ret = []
        for le in les:
            ret.append({'type': 'LogicalEnclosureV400', 'name': le['name']})
        return ret

    def create_san_manager_data(self, sans):
        ret = []
        for san in sans:
            if 'Brocade Network Advisor' in san['Type']:
                ret.append({'connectionInfo': [{'name': 'Type', 'value': san['Type']},
                                               {'name': 'Host', 'value': san['Host']},
                                               {'name': 'Port', 'value': san['Port']},
                                               {'name': 'Username', 'value': san['Username']},
                                               {'name': 'Password', 'value': san['Password']},
                                               {'name': 'UseSsl', 'value': san['UseSsl']}]})
            elif 'HPE' in san['Type']:
                ret.append({'connectionInfo': [{'name': 'Type', 'value': san['Type']},
                                               {'name': 'Host', 'value': san['Host']},
                                               {'name': 'SnmpPort', 'value': san['SnmpPort']},
                                               {'name': 'SnmpUserName', 'value': san['SnmpUserName']},
                                               {'name': 'SnmpAuthLevel', 'value': san['SnmpAuthLevel']},
                                               {'name': 'SnmpAuthProtocol', 'value': san['SnmpAuthProtocol']},
                                               {'name': 'SnmpAuthString', 'value': san['SnmpAuthString']},
                                               {'name': 'SnmpPrivProtocol', 'value': san['SnmpPrivProtocol']},
                                               {'name': 'SnmpPrivString', 'value': san['SnmpPrivString']}]})
            elif 'Cisco' in san['Type']:
                ret.append({'connectionInfo': [{'name': 'Type', 'value': san['Type']},
                                               {'name': 'Host', 'value': san['Host']},
                                               {'name': 'SnmpPort', 'value': san['SnmpPort']},
                                               {'name': 'SnmpUserName', 'value': san['SnmpUserName']},
                                               {'name': 'SnmpAuthString', 'value': san['SnmpAuthString']},
                                               {'name': 'SnmpAuthLevel', 'value': san['SnmpAuthLevel']},
                                               {'name': 'SnmpAuthProtocol', 'value': san['SnmpAuthProtocol']}]})
        return ret

    def get_expected_san_manager_data(self, sans):
        ret = []
        for san in sans:
            ret.append({'name': san['Host'], 'type': 'FCDeviceManagerV2'})
        return ret

    def create_ebulk_data(self, ethernets):
        ret = []
        for ethernet in ethernets:
            ret.append({"vlanIdRange": str(ethernet['vlanIdStart']) + '-' + str(ethernet['vlanIdEnd']), "purpose": ethernet['purpose'],
                        "namePrefix": ethernet['namePrefix'], "smartLink": ethernet['smartLink'], "privateNetwork": ethernet['privateNetwork'],
                        "bandwidth": ethernet['bandwidth'], "type": ethernet['type']})
        return ret

    def get_expected_ebulk_data(self, ethernets):
        ret = []
        for ethernet in ethernets:
            count = ethernet['vlanIdEnd'] - ethernet['vlanIdStart'] + 1
            for i in xrange(count):
                vlan_id = ethernet['vlanIdStart'] + i
                name = ethernet['namePrefix'] + '_' + str(vlan_id)
                ret.append({'name': name, 'type': 'ethernet-networkV300'})
        return ret

    def create_fcnet_data(self, fc_nets):
        ret = []
        for fc in fc_nets:
            for i in xrange(1, fc['count'] + 1):
                name = fc['base_name'] + str(i)
                ret.append({'name': name, 'autoLoginRedistribution': 'true', 'type': 'fc-networkV300', 'linkStabilityTime': '30',
                            'fabricType': 'FabricAttach', 'connectionTemplateUri': None, 'managedSanUri': 'FCSan:' + fc['associatedSAN']})
        return ret

    def get_expected_fcnet_data(self, fc_nets):
        ret = []
        for fc in fc_nets:
            for i in xrange(1, fc['count'] + 1):
                name = fc['base_name'] + str(i)
                ret.append({"type": "fc-networkV300", "name": name})
        return ret

    def create_fcoenet_data(self, fcoes):
        ret = []
        for fcoe in fcoes:
            for i in xrange(1, fcoe['count'] + 1):
                name = fcoe['base_name'] + str(i)
                ret.append({'name': name, 'type': 'fcoe-networkV300', 'vlanId': fcoe['vlanId'], 'managedSanUri': 'FCSan:' + fcoe['san']})
        return ret

    def get_expected_fcoenet_data(self, fcoes):
        ret = []
        for fcoe in fcoes:
            for i in xrange(1, fcoe['count'] + 1):
                name = fcoe['base_name'] + str(i)
                ret.append({'type': 'fcoe-networkV300', 'name': name})
        return ret

    def create_network_set_data(self, net_sets):
        base_name = 'Network_Set_'
        ret = []
        for net_set in net_sets:
            networkset_name = base_name + str(net_set['network_set'])
            network_uris = ["Ethernet" + '_' + str(net_set['start_vlan'] + i) for i in xrange(net_set['network_count'])]
            native_network_uri = network_uris[0]
            ret.append({'name': networkset_name, 'nativeNetworkUri': native_network_uri, 'type': 'network-setV300', 'networkUris': network_uris})
        return ret

    def get_expected_network_set_data(self, net_sets):
        base_name = 'Network_Set_'
        ret = []
        for net_set in net_sets:
            networkset_name = base_name + str(net_set['network_set'])
            ret.append({'name': networkset_name, 'type': 'network-setV300'})
        return ret

    def expected_storage_system(self, storage_systems):
        stor = []
        for storage in storage_systems:
            stor.append({'type': 'StorageSystemV4', 'name': storage['name']})
        return stor

    def storage_volumes(self, storage_volumes):
        vol = []
        for vols in storage_volumes:
            vol.append({"properties": {"name": vols['name'], "description": "non-boot private volume", "storagePool": vols['StoragePool'],
                                       "size": 1073741824, "provisioningType": "Thin", "isShareable": vols['share']},
                        "templateUri": 'ROOT', "isPermanent": True})
        return vol

    def expected_storage_volumes(self, storage_volumes):
        expectedVol = []
        for exp_vols in storage_volumes:
            expectedVol.append({'type': 'StorageVolumeV4', 'name': exp_vols['name']})
        return expectedVol

    def create_uplink_data(self, uplinks):
        uplink_set = {}
        for uplink in uplinks:
            if uplink['networkType'] == 'Ethernet':
                networkUri = []
                for i in xrange(uplink['networkUrisvlanIdStart'], uplink['networkUrisvlanIdEnd'] + 1):
                    network = "Ethernet_" + str(i)
                    networkUri.append(network)
            else:
                networkUri = uplink['networkUris']
            uplink_set.update({uplink['name']: {'name': uplink['name'], 'networkType': uplink['networkType'], 'ethernetNetworkType': uplink['ethernetNetworkType'],
                                                'networkUris': networkUri, 'logicalPortConfigInfos': uplink['logicalPortConfigInfos']}})
        return uplink_set

#     def make_server_profile_data(self, sps, spts):
#         ret = []
#         for sp in sps:
#             for spt in spts:
#                 if sp['serverProfileTemplateUri'] == spt['name']:
#                     enclosureGroupUri = spt['enclosureGroupUri']
#                     connections = spt['connectionSettings']['connections']
#                     ret.append({'name': sp['name'], 'type': 'ServerProfileV7',
#                                 'enclosureGroupUri': enclosureGroupUri,
#                                 'serverHardwareUri': sp['serverHardwareUri'], 'connections': connections, 'serverProfileTemplateUri': 'SPT:' + sp['serverProfileTemplateUri']})
#         return ret

#     def make_expected_server_profile_data(self, sps, spts):
#         ret = []
#         for sp in sps:
#             for spt in spts:
#                 if sp['serverProfileTemplateUri'] == spt['name']:
#                     enclosureGroupUri = spt['enclosureGroupUri']
#                     serverHardwareTypeUri = spt['serverHardwareTypeUri']
#                     connections = spt['connectionSettings']['connections']
#                     ret.append({'type': 'ServerProfileV7', 'serverHardwareUri': 'SH:' + sp['serverHardwareUri'], 'serverHardwareTypeUri': serverHardwareTypeUri,
#                                 'enclosureGroupUri': enclosureGroupUri, 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'description': None,
# 'name': sp['name'], 'connections': connections,# 'status': 'OK', 'state': 'Normal'
#                                 'localStorage': spt['localStorage'], 'sanStorage': spt['sanStorage']
#                                 })
#         return ret

    def make_expected_server_profile_data(self, sps):
        ret = []
        for sp in sps:
            ret.append({'type': 'ServerProfileV7', 'serverHardwareUri': 'SH:' + sp['serverHardwareUri'],
                        'name': sp['name'], 'status': 'OK', 'state': 'Normal'})
        return ret
