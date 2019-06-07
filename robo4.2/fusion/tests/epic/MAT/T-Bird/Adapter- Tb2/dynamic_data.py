class DynamicData(object):

    def _init_(self):
        # valid characters
        self.chars = [chr(x) for x in range(33, 127)]

    def get_spp_path(self, name, local_dir):
        local_path = local_dir + name + '.iso'
        return local_path

    def expected_spp_data(self, name):
        ret = []
        ret.append({'type': 'firmware-baselines', 'name': 'Service Pack for ProLiant'})
        return ret

    def spp_name_withunderscore(self, name):
        withunderscore = name.replace('.', '_')
        return withunderscore

    def users_data(self, users):
        user_data = []
        for user in users:
            user_data.append({'type': 'UserAndPermissions', 'userName': user['name'], 'password': 'Cosmos123', 'fullName': user['name'],
                              'emailAddress': user['name'] + '@hpe.com', 'officePhone': '970-898-2222', 'mobilePhone': '970-898-0022',
                              'permissions': [{'roleName': user['role'], 'scopeUri': None}], 'enabled': True})
        return user_data

    def expected_users_data(self, users):
        expected_user_data = []
        for user in users:
            expected_user_data.append({'userName': user['name'], 'fullName': user['name'], 'permissions': [{'roleName': user['role'], 'scopeUri': None}],
                                       'emailAddress': user['name'] + '@hpe.com', 'officePhone': '970-898-2222', 'mobilePhone': '970-898-0022', 'type': 'UserAndPermissions'})
        return expected_user_data

    def make_enc_group_data(self, enc_grps):
        ret = []
        for enc_grp in enc_grps:
            interconnect = []
            for x in range(1, enc_grp['enclosureCount'] + 1):
                for i in range(1, 7):
                    interconnect.append({'enclosureIndex': x, 'interconnectBay': i, 'logicalInterconnectGroupUri': enc_grp['interconnectBayMappings'][i - 1]['lig']})
            ret.append({'name': enc_grp['name'], 'type': 'EnclosureGroupV400', 'enclosureCount': enc_grp['enclosureCount'], 'stackingMode': 'Enclosure',
                        'interconnectBayMappings': interconnect, 'ipAddressingMode': enc_grp['ipAddressingMode'], 'powerMode': 'RedundantPowerFeed'})
        return ret

    def make_expected_enc_group_data(self, enc_grps):
        ret = []
        for enc_grp in enc_grps:
            ret.append({'name': enc_grp['name'], 'type': 'EnclosureGroupV400', 'enclosureCount': enc_grp['enclosureCount'],
                        'stackingMode': 'Enclosure', 'powerMode': enc_grp['powerMode'], 'interconnectBayMappings': enc_grp['interconnectBayMappings']})
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

    def get_expected_ethernet_data(self, ethernets):
        ret = []
        for ethernet in ethernets:
            ret.append({'name': ethernet['name'], 'type': ethernet['type'], 'vlanId': ethernet['vlanId'], 'purpose': ethernet['purpose'],
                        'smartLink': ethernet['smartLink'], 'privateNetwork': ethernet['privateNetwork']})
        return ret

    def get_expected_fcnet_data(self, fc_nets):
        ret = []
        for fc in fc_nets:
            ret.append({'type': fc['type'], 'name': fc['name'], 'fabricType': fc['fabricType'], 'managedSanUri': fc['managedSanUri']})
        return ret

    def get_expected_fcoenet_data(self, fcoe_nets):
        ret = []
        for fcoe in fcoe_nets:
            ret.append({'type': fcoe['type'], 'name': fcoe['name'], 'vlanId': fcoe['vlanId'], 'managedSanUri': fcoe['managedSanUri']})
        return ret

    def get_expected_network_set_data(self, net_sets):
        ret = []
        for net_set in net_sets:
            networkUri = []
            for uri in net_set['networkUris']:
                networkUri.append('ETH:' + uri)
            ret.append({'name': net_set['name'], 'type': net_set['type'], 'networkUris': networkUri, 'nativeNetworkUri': net_set['nativeNetworkUri']})
        return ret

    def expected_storage_system(self, storage_systems):
        stor = []
        for storage in storage_systems:
            stor.append({'type': 'StorageSystemV4', 'name': storage['name'], 'status': 'OK', 'state': 'Managed'})
        return stor

    def existing_storage_volumes(self, storage_volumes):
        vol = []
        for vols in storage_volumes:
            vol.append({'storageSystemUri': vols['storageSystemUri'], 'deviceVolumeName': vols['name'],
                        'name': vols['name'], 'isShareable': False})
        return vol

    def expected_storage_volumes(self, storage_volumes):
        expectedVol = []
        for exp_vols in storage_volumes:
            expectedVol.append({'type': 'StorageVolumeV5', 'name': exp_vols['name'], 'status': 'OK', 'state': 'Managed'})
        return expectedVol

    def make_server_profile_data(self, sps, firmware):
        ret = []
        for sp in sps:
            ret.append({'name': sp['name'], 'type': 'ServerProfileV8', 'serverHardwareUri': sp['serverHardwareUri'],
                        'serverHardwareTypeUri': sp['serverHardwareTypeUri'],  # 'enclosureUri': sp['enclosureUri'],
                        'enclosureGroupUri': sp['enclosureGroupUri'], 'description': '', 'affinity': 'Bay',
                        'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                        'bootMode': sp['bootMode'], 'boot': sp['boot'], 'connectionSettings': sp['connectionSettings'],
                        # 'firmware': {'manageFirmware': firmware['manageFirmware'],
                        #             'forceInstallFirmware': firmware['forceInstallFirmware'], 'firmwareInstallType': firmware['firmwareInstallType']},
                        'localStorage': sp['localStorage'], 'sanStorage': sp['sanStorage'], 'bios': sp['bios']})
        return ret

    def make_expected_server_profile_data(self, sps, firmware):
        import copy
        ret = []
        for sp in sps:
            sanStorage = copy.deepcopy(sp['sanStorage'])
            for vol in sanStorage['volumeAttachments']:
                if 'volumeUri' in vol:
                    if vol['volumeUri'] is None:
                        vol['volumeUri'] = 'SVOL:' + vol['volumeName']
                if 'volumeName' in vol:
                    del vol['volumeName']
                if 'volumeShareable' in vol:
                    del vol['volumeShareable']
                if 'volumeProvisionedCapacityBytes' in vol:
                    del vol['volumeProvisionedCapacityBytes']
                if 'volumeProvisionType' in vol:
                    del vol['volumeProvisionType']
                if 'permanent' in vol:
                    del vol['permanent']
                if 'storagePaths' in vol:
                    del vol['storagePaths']

            ret.append({'name': sp['name'], 'type': 'ServerProfileV8', 'serverHardwareUri': sp['serverHardwareUri'],
                        'enclosureGroupUri': 'EG:' + sp['enclosureGroupUri'],
                        'connectionSettings': sp['connectionSettings'], 'status': 'OK', 'state': 'Normal', 'bootMode': sp['bootMode'], 'boot': sp['boot'], 'bios': sp['bios'],
                        'localStorage': sp['localStorage'], 'sanStorage': sanStorage})
        return ret

    def make_expected_unassign_server_profile_data(self, sps, firmware):
        import copy
        ret = []
        for sp in sps:
            sanStorage = copy.deepcopy(sp['sanStorage'])
            for vol in sanStorage['volumeAttachments']:
                if 'volumeUri' in vol:
                    if vol['volumeUri'] is None:
                        vol['volumeUri'] = 'SVOL:' + vol['volumeName']
                if 'volumeName' in vol:
                    del vol['volumeName']
                if 'volumeShareable' in vol:
                    del vol['volumeShareable']
                if 'volumeProvisionedCapacityBytes' in vol:
                    del vol['volumeProvisionedCapacityBytes']
                if 'volumeProvisionType' in vol:
                    del vol['volumeProvisionType']
                if 'permanent' in vol:
                    del vol['permanent']
                if 'storagePaths' in vol:
                    del vol['storagePaths']

            ret.append({'name': sp['name'], 'type': 'ServerProfileV8', 'serverHardwareUri': None,
                        'enclosureGroupUri': 'EG:' + sp['enclosureGroupUri'],
                        'connectionSettings': sp['connectionSettings'], 'status': 'OK', 'state': 'Normal', 'bootMode': sp['bootMode'], 'boot': sp['boot'], 'bios': sp['bios'],
                        'localStorage': sp['localStorage'], 'sanStorage': sanStorage})
        return ret

    def make_expected_logical_enclosure_data(self, les):
        ret = []
        for le in les:
            ret.append({'type': 'LogicalEnclosureV400', 'name': le['name'], 'status': 'OK',
                        'enclosureUris': le['enclosureUris'], 'enclosureGroupUri': le['enclosureGroupUri']})
        return ret
