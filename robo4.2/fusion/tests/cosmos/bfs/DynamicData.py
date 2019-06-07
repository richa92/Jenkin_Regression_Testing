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

    def make_expected_lig_data(self, ligs):
        ret = []
        for lig in ligs:
            ret.append({'name': lig['name'], 'type': 'logical-interconnect-groupV6'})
        return ret

    def make_enc_group_data(self, enc_grps):
        ret = []
        for enc_grp in enc_grps:
            interconnect = []
            for x in range(1, enc_grp['enclosureCount'] + 1):
                for i in range(1, 7):
                    interconnect.append({'enclosureIndex': x, 'interconnectBay': i, 'logicalInterconnectGroupUri': enc_grp['interconnectBayMappings'][i - 1]['lig']})
            ret.append({'name': enc_grp['name'], 'enclosureCount': enc_grp['enclosureCount'],
                        'interconnectBayMappings': interconnect, 'ipAddressingMode': enc_grp['ipAddressingMode'], 'powerMode': 'RedundantPowerFeed'})
        return ret

    def make_expected_enc_group_data(self, enc_grps):
        ret = []
        for enc_grp in enc_grps:
            ret.append({'name': enc_grp['name'], 'enclosureCount': enc_grp['enclosureCount'],
                        'powerMode': enc_grp['powerMode'], 'interconnectBayMappings': enc_grp['interconnectBayMappings']})
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

    def expected_storage_system(self, storage_systems):
        stor = []
        for storage in storage_systems:
            stor.append({'type': 'StorageSystemV5', 'name': storage['name'], 'status': 'OK', 'state': 'Managed'})
        return stor

    def get_expected_iscsi_data(self, iscsi_nets):
        ret = []
        for iscsi in iscsi_nets:
            ret.append({"vlanId": iscsi['vlanId'], "ethernetNetworkType": "Tagged", "purpose": "ISCSI", "name": iscsi['name'], "smartLink": True, "privateNetwork": False, "type": "ethernet-networkV4"})
        return ret

    def existing_storage_volumes(self, storage_volumes):
        vol = []
        for vols in storage_volumes:
            vol.append({'storageSystemUri': vols['storageSystemUri'], 'deviceVolumeName': vols['name'],
                        'name': vols['name'], 'isShareable': False})
        return vol

    def expected_storage_volumes(self, storage_volumes):
        expectedVol = []
        for exp_vols in storage_volumes:
            expectedVol.append({'type': 'StorageVolumeV8', 'name': exp_vols['name'], 'status': 'OK', 'state': 'Managed'})
        return expectedVol

    def make_enclosure_data(self, encls):
        ret = []
        for encl in encls:
            ret.append({'enclosureGroupUri': encl['enclosureGroupUri'], 'hostname': encl['hostname'], 'name': encl['name'],
                        'username': encl['username'], 'password': encl['password'], 'licensingIntent': encl['licensingIntent'],
                        'firmwareBaselineUri': encl['firmwareBaselineUri'], 'updateFirmwareOn': encl['updateFirmwareOn'],
                        'forceInstallFirmware': encl['forceInstallFirmware'], 'force': encl['force']})
        return ret

    def make_expected_enclosure_data(self, encls):
        ret = []
        for encl in encls:
            ret.append({'type': 'EnclosureV8', 'name': encl['name'], 'status': 'OK', 'state': 'Configured',
                        'logicalEnclosureUri': 'LE:' + encl['name']})
        return ret

    def make_expected_server_profile_data(self, sps, firmware, unassign=None):
        ret = []
        for sp in sps:
            if unassign:
                sp['serverHardwareUri'] = None
            ret.append({'name': sp['name'], 'type': 'ServerProfileV11', 'serverHardwareUri': sp['serverHardwareUri'],
                        'enclosureGroupUri': sp['enclosureGroupUri'],
                        'serverHardwareTypeUri': sp['serverHardwareTypeUri'],
                        'firmware': {'firmwareInstallType': firmware['firmwareInstallType'], 'forceInstallFirmware': False, 'manageFirmware': firmware['manageFirmware'], 'firmwareBaselineUri': firmware['firmwareBaselineUri']},
                        'connectionSettings': sp['connectionSettings'], 'state': 'Normal', 'bootMode': sp['bootMode'], 'boot': sp['boot'], 'bios': sp['bios'],
                        'localStorage': sp['localStorage'], 'sanStorage': sp['sanStorage']
                        })
        return ret

    def make_server_profile_data(self, sps, firmware):
        ret = []
        for sp in sps:
            ret.append({'name': sp['name'], 'type': 'ServerProfileV11', 'serverHardwareUri': sp['serverHardwareUri'],
                        'enclosureGroupUri': sp['enclosureGroupUri'],
                        'serverHardwareTypeUri': sp['serverHardwareTypeUri'],
                        'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual',
                        'firmware': {'firmwareInstallType': firmware['firmwareInstallType'], 'forceInstallFirmware': firmware['forceInstallFirmware'], 'manageFirmware': firmware['manageFirmware'], 'firmwareBaselineUri': firmware['firmwareBaselineUri']},
                        'connectionSettings': sp['connectionSettings'], 'bootMode': sp['bootMode'], 'boot': sp['boot'], 'bios': sp['bios'],
                        'localStorage': sp['localStorage'], 'sanStorage': sp['sanStorage']
                        })
        return ret

    def make_server_profile_add_volume_data(self, sps, firmware, storage_system, add_volume):
        ret = []
        for sp in sps:
            add_vol_body = {'id': 2, 'volumeStorageSystemUri': storage_system, 'lunType': 'Auto', 'volumeUri': add_volume, 'bootVolumePriority': 'NotBootable', 'storagePaths': [{'isEnabled': True, 'connectionId': 3, 'targetSelector': 'Auto'}, {'isEnabled': True, 'connectionId': 4, 'targetSelector': 'Auto'}]}
            sp['sanStorage']['volumeAttachments'].append(add_vol_body)
            ret.append({'name': sp['name'], 'type': 'ServerProfileV11', 'serverHardwareUri': sp['serverHardwareUri'],
                        'enclosureGroupUri': sp['enclosureGroupUri'],
                        'serverHardwareTypeUri': sp['serverHardwareTypeUri'],
                        'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual',
                        'firmware': {'firmwareInstallType': firmware['firmwareInstallType'], 'forceInstallFirmware': firmware['forceInstallFirmware'], 'manageFirmware': firmware['manageFirmware'], 'firmwareBaselineUri': firmware['firmwareBaselineUri']},
                        'connectionSettings': sp['connectionSettings'], 'bootMode': sp['bootMode'], 'boot': sp['boot'], 'bios': sp['bios'],
                        'localStorage': sp['localStorage'], 'sanStorage': sp['sanStorage']
                        })
        return ret

    def make_downlink_disable(self, disable, status):
        ret = []
        for dis in disable:
            body = {"portType": "Downlink", "portHealthStatus": "Disabled", "enabled": False, "portStatus": "Unlinked", "type": "portV6"}
            body.update(dis)
            ret.append({'name': dis['interconnectName'], "port": dis['portId'], 'downlink': body, 'inter_status': status, 'port_status': body['portStatus']})
        return ret

    def make_downlink_enable(self, enable, status):
        ret = []
        for en in enable:
            body = {"portType": "Downlink", "portHealthStatus": "Normal", "enabled": True, "portStatus": "Linked", "type": "portV6"}
            body.update(en)
            ret.append({'name': en['interconnectName'], "port": en['portId'], 'downlink': body, 'inter_status': status, 'port_status': body['portStatus']})
        return ret

    def make_uplink_disable(self, disable, status):
        ret = []
        for dis in disable:
            body = {"portType": "Uplink", "portHealthStatus": "Disabled", "enabled": False, "portStatus": "Unlinked", "type": "portV6"}
            body.update(dis)
            ret.append({'name': dis['interconnectName'], "port": dis['portId'], 'uplink': body, 'inter_status': status, 'port_status': body['portStatus']})
        return ret

    def make_uplink_enable(self, enable, status):
        ret = []
        for en in enable:
            body = {"portType": "Uplink", "portHealthStatus": "Normal", "enabled": True, "portStatus": "Linked", "type": "portV6"}
            body.update(en)
            ret.append({'name': en['interconnectName'], "port": en['portId'], 'uplink': body, 'inter_status': status, 'port_status': body['portStatus']})
        return ret
