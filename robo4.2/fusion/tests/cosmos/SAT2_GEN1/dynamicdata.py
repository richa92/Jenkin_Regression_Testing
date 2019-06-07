'''
SAT SYNERGY RING2 GEN1 Dynamic Data File

'''

import re


class DynamicData(object):
    """Class for Dynamic Data"""

    def _init_(self):
        """valid characters"""
        self.chars = [chr(x) for x in range(33, 127)]

    def rename_enclosure(self, enclosures):
        """Rename Enclosure"""
        ret = []
        for enc in enclosures:
            ret.append({"op": "replace", "path": "/name", "value": enc['newName'], "name": enc['serialNumber']})
        return ret

    def expected_enclosure_data(self, enclosures):
        """Generate Expected Enclosure Data"""
        ret = []
        for enc in enclosures:
            ret.append({'name': enc['newName'], 'serialNumber': enc['serialNumber'], 'type': 'EnclosureV7'})
        return ret

    def get_expected_scope_data(self, scopes):
        """Make Expected Scope Data"""
        ret = []
        for scope in scopes:
            ret.append({"name": scope['name'], "type": scope['type']})
        return ret

    def get_spp_path(self, name, local_dir):
        """Get spp path"""
        local_path = local_dir + name + '.iso'
        return local_path

    def spp_name_withunderscore(self, name):
        """Return spp name by replacing with underscore"""
        withunderscore = name.replace('.', '_')
        return withunderscore

    def get_spp_details(self, spps):
        """Get spp details"""
        ret = []
        for spp in spps:
            ret.append({"local_path": spp['localpath'] + spp['name'] + '.iso',
                        "updatedname": self.spp_name_withunderscore(spp['name'])})
        return ret

    def make_server_leaf_certificate_dict(self, leaf_certificate):
        """Make server leaf certificate dictionary"""
        ret = []
        for cert in leaf_certificate:
            ret.append({
                'name': cert['aliasName'],
                'type': 'CertificateInfoV2',
                'certificateDetails':
                [
                    {
                        'base64Data': cert['base64Data'],
                        'aliasName': cert['aliasName'],
                        'type': 'CertificateDetailV2'
                    },
                ]
            })
        return ret

    def make_expected_server_leaf_certificate(self, expected_leaf_certificate):
        """Make expected server leaf certificate data dictionary"""
        ret = []
        for cert in expected_leaf_certificate:
            ret.append({
                'name': cert['aliasName'],
                'type': 'CertificateInfoV2',
                'certificateDetails':
                [
                    {
                        'aliasName': cert['aliasName'],
                        'type': 'CertificateDetailV2'
                    },
                ]
            })
        return ret

    def make_ad_dict(self, ads):
        """Make active directory data dictionary"""
        ret = []
        for ad in ads:
            ret.append({'type': 'LoginDomainConfigV600', "directoryBindingType": "USER_ACCOUNT", 'name': ad['name'],
                        'authProtocol': 'AD', 'orgUnits': [],
                        'userNamingAttribute': 'UID', 'baseDN': ad['baseDN'],
                        'credential': {'userName': ad['userName'], 'password': ad['password']},
                        'directoryServers': [{'type': 'LoginDomainDirectoryServerInfoDto',
                                              'directoryServerSSLPortNumber': ad['directoryServerSSLPortNumber'],
                                              'directoryServerIpAddress': ad['directoryServerIpAddress'],
                                              'directoryServerCertificateStatus': '',
                                              'serverStatus': '',
                                              'directoryServerCertificateBase64Data': ad[
                                                  'directoryServerCertificateBase64Data']}]})
        return ret

    def make_expected_ad_dict(self, expected_ad):
        """Make expected active directory data dictionary"""
        expected_ad_data = []
        for ads in expected_ad:
            expected_ad_data.append({'type': 'LoginDomainConfigV600', 'name': ads['name'], 'authProtocol': 'AD',
                                     'baseDN': ads['baseDN'],
                                     'directoryServers': [{'type': 'LoginDomainDirectoryServerInfoDto',
                                                           'directoryServerSSLPortNumber': ads[
                                                               'directoryServerSSLPortNumber'],
                                                           'directoryServerIpAddress': ads['directoryServerIpAddress'],
                                                           'serverStatus': 'OK',
                                                           }]})
        return expected_ad_data

    def make_ad_group_data(self, adgroups):
        """Make active directory group data dictionary"""
        ad_group_data = []
        for adgroup in adgroups:
            permissions = []
            for permission in adgroup['permissions']:
                permissions.append(permission)
            ad_group_data.append({
                "credentials": {
                    "password": adgroup['password'],
                    "userName": adgroup['userName'],
                },
                "group2PermissionPerGroup": {
                    "egroup": adgroup['egroup'],
                    "loginDomain": adgroup['loginDomain'],
                    "permissions": permissions,
                    "type": "LoginDomainGroupPermission"
                },
                "type": "LoginDomainGroupCredentials"
            })
        return ad_group_data

    def make_expected_ad_group_data(self, adgroups):
        """Make expected active directory group data dictionary"""
        expected_ad_group_data = []
        for adgroup in adgroups:
            permissions = []
            for permission in adgroup['permissions']:
                permissions.append(permission)
            expected_ad_group_data.append({'category': 'users', 'egroup': adgroup['egroup'],
                                           "permissions": permissions,
                                           'loginDomain': adgroup['loginDomain'],
                                           'type': 'LoginDomainGroupPermission'})
        return expected_ad_group_data

    def make_lig_data(self, ligs):
        """Make lig data dictionary"""
        ret = []
        for lig in ligs:
            ret.append({"name": lig['name'],
                        "type": "logical-interconnect-groupV5",
                        "enclosureType": "C7000",
                        "ethernetSettings": None,
                        "description": None,
                        "status": None,
                        "state": None,
                        "category": None,
                        "created": None,
                        "modified": None,
                        "eTag": None,
                        "uri": None,
                        "uplinkSets": lig['uplinkSets'],
                        'interconnectMapTemplate': lig["interconnectMapTemplate"],
                        "internalNetworkUris": [],
                        "qosConfiguration": {
                            "activeQosConfig": {"type": "QosConfiguration", "configType": "Passthrough",
                                                "downlinkClassificationType": None, "uplinkClassificationType": None,
                                                "qosTrafficClassifiers": None, "description": None, "status": None,
                                                "name": None, "state": None, "category": "qos-aggregated-configuration",
                                                "created": None, "modified": None, "eTag": None, "uri": None},
                            "inactiveFCoEQosConfig": None, "inactiveNonFCoEQosConfig": None,
                            "type": "qos-aggregated-configuration", "name": None, "state": None, "status": None,
                            "eTag": None, "modified": None, "created": None, "category": "qos-aggregated-configuration",
                            "uri": None}
                        })
        return ret

    def make_expected_lig_data(self, ligs):
        """Make expected lig data dictionary"""
        ret = []
        for lig in ligs:
            uplink_sets = []
            for us in lig['uplinkSets']:
                uplink_set = {'name': us['name']}
                if "Ethernet" == us["networkType"]:
                    prefix = "ETH:"
                elif "FibreChannel" == us["networkType"]:
                    prefix = "FC:"
                net_uris = [prefix + net_uri for net_uri in us["networkUris"]]
                uplink_set["networkUris"] = net_uris
                uplink_sets.append(uplink_set)
            ret.append(
                {'name': lig['name'], 'type': 'logical-interconnect-groupV5', 'enclosureType': lig['enclosureType'],
                 'uplinkSets': uplink_sets})
        return ret

    def make_enc_group_data(self, enc_grps):
        """Make encosure group data dictionary"""
        ret = []
        for enc_grp in enc_grps:
            interconnect = []
            for x in range(1, enc_grp['enclosureCount'] + 1):
                for i in range(1, 7):
                    interconnect.append({'enclosureIndex': x, 'interconnectBay': i,
                                         'logicalInterconnectGroupUri': enc_grp['interconnectBayMappings'][i - 1][
                                             'lig']})
            ret.append({'name': enc_grp['name'], 'enclosureCount': enc_grp['enclosureCount'],
                        'interconnectBayMappings': interconnect, 'ipAddressingMode': enc_grp['ipAddressingMode'],
                        'powerMode': 'RedundantPowerFeed'})
        return ret

    def make_expected_enc_group_data(self, enc_grps):
        """Make expected enclosure group data dictionary"""
        ret = []
        for enc_grp in enc_grps:
            ret.append({'name': enc_grp['name'],
                        'interconnectBayMappings': enc_grp['interconnectBayMappings'], "status": "OK"})
        return ret

    def create_san_manager_data(self, sans):
        """Make san manager data dictionary"""
        ret = []
        for san in sans:
            if 'Brocade Network Advisor' in san['Type']:
                ret.append({'connectionInfo': [{'name': 'Type', 'value': san['Type']},
                                               {'name': 'Host',
                                                   'value': san['Host']},
                                               {'name': 'Port',
                                                   'value': san['Port']},
                                               {'name': 'Username',
                                                   'value': san['Username']},
                                               {'name': 'Password',
                                                   'value': san['Password']},
                                               {'name': 'UseSsl', 'value': san['UseSsl']}]})
            elif 'HPE' in san['Type']:
                ret.append({'connectionInfo': [{'name': 'Type', 'value': san['Type']},
                                               {'name': 'Host',
                                                   'value': san['Host']},
                                               {'name': 'SnmpPort',
                                                   'value': san['SnmpPort']},
                                               {'name': 'SnmpUserName',
                                                   'value': san['SnmpUserName']},
                                               {'name': 'SnmpAuthLevel',
                                                   'value': san['SnmpAuthLevel']},
                                               {'name': 'SnmpAuthProtocol',
                                                   'value': san['SnmpAuthProtocol']},
                                               {'name': 'SnmpAuthString',
                                                   'value': san['SnmpAuthString']},
                                               {'name': 'SnmpPrivProtocol',
                                                   'value': san['SnmpPrivProtocol']},
                                               {'name': 'SnmpPrivString', 'value': san['SnmpPrivString']}]})
            elif 'Cisco' in san['Type']:
                ret.append({'connectionInfo': [{'name': 'Type', 'value': san['Type']},
                                               {'name': 'Host',
                                                   'value': san['Host']},
                                               {'name': 'SnmpPort',
                                                   'value': san['SnmpPort']},
                                               {'name': 'SnmpUserName',
                                                   'value': san['SnmpUserName']},
                                               {'name': 'SnmpAuthString',
                                                   'value': san['SnmpAuthString']},
                                               {'name': 'SnmpAuthLevel',
                                                   'value': san['SnmpAuthLevel']},
                                               {'name': 'SnmpAuthProtocol', 'value': san['SnmpAuthProtocol']}]})
        return ret

    def get_expected_san_manager_data(self, sans):
        """Get expected san manager data dictionary"""
        ret = []
        for san in sans:
            ret.append({'name': san['Host'], 'type': 'FCDeviceManagerV2'})
        return ret

    def get_expected_ethernet_data(self, ethernets):
        """Get expected ethernet data dictionary"""
        ret = []
        for ethernet in ethernets:
            ret.append({'name': ethernet['name'], 'type': ethernet['type'], 'vlanId': ethernet['vlanId'],
                        'purpose': ethernet['purpose'],
                        'smartLink': ethernet['smartLink'], 'privateNetwork': ethernet['privateNetwork']})
        return ret

    def get_ethernet_name_data(self, ethernets):
        """Get ethernet name data"""
        ret = []
        for ethernet in ethernets:
            count = ethernet['vlanIdEnd'] - ethernet['vlanIdStart'] + 1
            for i in xrange(count):
                vlan_id = ethernet['vlanIdStart'] + i
                name = ethernet['namePrefix'] + '_' + str(vlan_id)
                ret.append(
                    {'name': name})
        return ret

    def make_untagged_tunnel_data(self, eths):
        """Make untagged tunnel data dictionary"""
        ret = []
        for eth in eths:
            for i in range(10):
                ret.append({"vlanId": 0, "ethernetNetworkType": eth['ethernetNetworkType'], "subnetUri": None,
                            "purpose": "General",
                            "name": eth['name'] + '_' + format(i), "smartLink": True, "privateNetwork": False,
                            "connectionTemplateUri": None, "type": "ethernet-networkV4"})
        return ret

    def make_expected_untagged_tunnel_data(self, eths):
        """Make expected untagged tunnel data dictionary"""
        ret = []
        for eth in eths:
            for i in range(10):
                ret.append({"vlanId": 0, "ethernetNetworkType": eth['ethernetNetworkType'], "purpose": "General",
                            "name": eth['name'] + '_' + format(i), "smartLink": True, "privateNetwork": False,
                            "type": "ethernet-networkV4"})
        return ret

    def create_ebulk_data(self, ethernets):
        """Create ethernet bulk data dictionary"""
        ret = []
        for ethernet in ethernets:
            ret.append({"vlanIdRange": str(ethernet['vlanIdStart']) + '-' + str(ethernet['vlanIdEnd']),
                        "purpose": ethernet['purpose'],
                        "namePrefix": ethernet['namePrefix'], "smartLink": ethernet['smartLink'],
                        "privateNetwork": ethernet['privateNetwork'],
                        "bandwidth": ethernet['bandwidth'], "type": ethernet['type']})
        return ret

    def get_expected_ebulk_data(self, ethernets):
        """Get expected ethernet bulk data dictionary"""
        ret = []
        for ethernet in ethernets:
            count = ethernet['vlanIdEnd'] - ethernet['vlanIdStart'] + 1
            for i in xrange(count):
                vlan_id = ethernet['vlanIdStart'] + i
                name = ethernet['namePrefix'] + '_' + str(vlan_id)
                ret.append(
                    {'name': name, 'type': 'ethernet-networkV4', 'status': 'OK'})
        return {'members': ret}

    def create_fcnet_data(self, fc_nets):
        """Create FC networks data dictionary"""
        ret = []
        for fc in fc_nets:
            for i in xrange(1, fc['count'] + 1):
                name = fc['base_name'] + str(i)
                ret.append({'name': name, 'autoLoginRedistribution': 'true', 'type': 'fc-networkV4',
                            'linkStabilityTime': '30',
                            'fabricType': 'FabricAttach', 'connectionTemplateUri': None,
                            'managedSanUri': 'FCSan:' + fc['associatedSAN']})
        return ret

    def get_expected_fcnet_data(self, fc_nets):
        """Get expected FC networks data dictionary"""
        ret = []
        for fc in fc_nets:
            ret.append({'type': fc['type'], 'name': fc['name'], 'fabricType': fc['fabricType'],
                        'managedSanUri': fc['managedSanUri']})
        return ret

    def create_fcoenet_data(self, fcoes):
        """Create FCoE network data dictionary"""
        ret = []
        for fcoe in fcoes:
            for i in xrange(1, fcoe['count'] + 1):
                name = fcoe['base_name'] + str(i)
                ret.append({'name': name, 'type': 'fcoe-networkV4', 'vlanId': fcoe['vlanId'],
                            'managedSanUri': 'FCSan:' + fcoe['san']})
        return ret

    def get_expected_fcoenet_data(self, fcoe_nets):
        """Get expected FCoE network data dictionary"""
        ret = []
        for fcoe in fcoe_nets:
            ret.append({'type': fcoe['type'], 'name': fcoe['name'], 'vlanId': fcoe['vlanId'],
                        'managedSanUri': fcoe['managedSanUri']})
        return ret

    def create_bulk_network_set_data(self, ns):
        """Create bulk network data dictionary"""
        network_sets = []
        for nss in ns:
            for i in range(0, nss['count']):
                ncount = nss['netNameSuffix'] + i * nss['netPerNS']
                network_sets.append({'name': nss['namePrefix'] + str(i), 'type': 'network-setV4',
                                     'networkUris': [nss['netNamePrefix'] + str(j) for j in
                                                     range(ncount, ncount + nss['netPerNS'])], 'nativeNetworkUri': nss['nativeNetworkUri']})
        return network_sets

    def get_expected_network_set_data(self, net_sets):
        """Get expected network set data dictionary"""
        ret = []
        for net_set in net_sets:
            network_uris = []
            for uri in net_set['networkUris']:
                network_uris.append('ETH:' + uri)
            if net_set['nativeNetworkUri']:
                nativeNetwork = 'ETH:' + net_set['nativeNetworkUri']
            else:
                nativeNetwork = None
            ret.append({'name': net_set['name'], 'type': net_set['type'], 'networkUris': network_uris,
                        'nativeNetworkUri': nativeNetwork})
        return ret

    def make_storage_system_with_pools_data(self, storagesystem):
        """Make storage system with pools data dictionary"""
        storage_system_pools = []
        for ssp in storagesystem:
            storage_system_pools.append({'name': ssp['name'], 'family': 'StoreServ', "hostname": ssp['hostname'],
                                         "credentials": {"username": ssp['username'], "password": ssp['password']},
                                         "serialNumber": ssp['serialNumber'],
                                         'deviceSpecificAttributes': {'managedDomain': ssp['managedDomain'],
                                                                      'managedPools': ssp['managedPools']}})
        return storage_system_pools

    def make_expected_storage_system_with_pools_data(self, storagesystem):
        """Make expected storage system with pools data dictionary"""
        expected_storage_system_pools = []
        for exp_ssp in storagesystem:
            expected_storage_system_pools.append(
                {'type': 'StorageSystemV4', 'name': exp_ssp['name'], 'uri': 'SSYS:' + exp_ssp['name'],
                 'state': 'Managed',
                 'deviceSpecificAttributes': {"managedDomain": exp_ssp['managedDomain'],
                                              "serialNumber": exp_ssp['serialNumber']},
                 'status': 'OK', 'category': 'storage-systems'})
        return expected_storage_system_pools

    def make_storage_pools_toedit_data(self, poolstoedit):
        """Make storage pools to edit data dictionary"""
        storage_pools_toedit = []
        for pool in poolstoedit:
            storage_pools_toedit.append(
                {"storageSystemUri": pool['storageSystemUri'], "name": pool['name'], "isManaged": True})
        return storage_pools_toedit

    def make_storage_volume_templates_data(self, storage_templates):
        """Make storage volume templates data dictionary"""
        storage_volume_templates = []
        for template in storage_templates:
            storage_volume_templates.append(
                {"name": template['name'], "rootTemplateUri": "SVT:" + template['name'],
                 "description": "private non-boot volume template",
                 "properties": {
                     "name": {"title": "Volume name", "description": "A volume name between 1 and 100 characters",
                              "type": "string", "minLength": 1, "maxLength": 100, "required": True,
                              "meta": {"locked": False}},
                     "description": {"title": "Description", "description": "A description for the volume",
                                     "type": "string", "minLength": 0, "maxLength": 2000, "default": "",
                                     "meta": {"locked": False}},
                     "storagePool": {"title": "Storage Pool",
                                     "description": "A common provisioning group URI reference",
                                     "type": "string", "required": True, "format": "x-uri-reference",
                                     "meta": {"locked": False, "createOnly": True,
                                              "semanticType": "device-storage-pool"},
                                     "default": template['default']},
                     "size": {"title": "Capacity", "description": "The capacity of the volume in bytes",
                              "type": "integer", "required": True, "minimum": 1073741824, "maximum": 17592186044416,
                              "meta": {"locked": False, "semanticType": "capacity"}, "default": 1073741824, },
                     "isShareable": {"title": "Is Shareable", "description": "The shareability of the volume",
                                     "type": "boolean", "meta": {"locked": False}, "default": False, },
                     "provisioningType": {"title": "Provisioning Type",
                                          "description": "The provisioning type for the volume",
                                          "type": "string", "enum": ["Thin", "Full"],
                                          "meta": {"locked": True, "createOnly": True},
                                          "default": "Thin"},
                     "snapshotPool": {"title": "Snapshot Pool",
                                      "description": "A URI reference to the common provisioning group used to create "
                                                     "snapshots",
                                      "type": "string", "format": "x-uri-reference",
                                      "meta": {"locked": True, "semanticType": "device-snapshot-storage-pool"},
                                      "default": template['default']}}})
        return storage_volume_templates

    def make_expected_storage_volume_template_data(self, storage_templates):
        """Make expected storage volume template data dictionary"""
        expected_storage_volume_template = []
        for exp_template in storage_templates:
            expected_storage_volume_template.append(
                {"category": "storage-volume-templates", "name": exp_template['name'], "status": "OK",
                 "state": "Configured", "type": "StorageVolumeTemplateV6", "uri": "SVT:" + exp_template['name'],
                 "properties": {
                     "name": {"title": "Volume name", "description": "A volume name between 1 and 100 characters",
                              "type": "string", "minLength": 1, "maxLength": 100, "required": True,
                              "meta": {"locked": False}},
                     "description": {"title": "Description", "description": "A description for the volume",
                                     "type": "string", "minLength": 0, "maxLength": 2000, "default": "",
                                     "meta": {"locked": False}},
                     "storagePool": {"title": "Storage Pool",
                                     "description": "A common provisioning group URI reference",
                                     "type": "string", "required": True, "format": "x-uri-reference",
                                     "meta": {"locked": False, "createOnly": True,
                                              "semanticType": "device-storage-pool"},
                                     "default": "SPOOL:" + exp_template['default']},
                     "size": {"title": "Capacity", "description": "The capacity of the volume in bytes",
                              "type": "integer", "required": True, "minimum": 1073741824, "maximum": 17592186044416,
                              "meta": {"locked": False, "semanticType": "capacity"}, "default": 1073741824},
                     "isShareable": {"title": "Is Shareable", "description": "The shareability of the volume",
                                     "type": "boolean", "meta": {"locked": False}, "default": False, },
                     "provisioningType": {"title": "Provisioning Type",
                                          "description": "The provisioning type for the volume",
                                          "type": "string", "enum": ["Thin", "Full"],
                                          "meta": {"locked": True, "createOnly": True},
                                          "default": "Thin"},
                     "snapshotPool": {"title": "Snapshot Pool",
                                      "description": "A URI reference to the common provisioning group used to create "
                                                     "snapshots",
                                      "type": "string", "format": "x-uri-reference",
                                      "meta": {"locked": True, "semanticType": "device-snapshot-storage-pool"},
                                      "default": "SPOOL:" + exp_template['default']}}})
        return expected_storage_volume_template

    def expected_storage_system(self, storage_systems):
        """Make expected storage system data dictionary"""
        stor = []
        for storage in storage_systems:
            stor.append({'type': 'StorageSystemV4',
                         'name': storage['name'], 'status': 'OK', 'state': 'Managed'})
        return stor

    def storage_volumes(self, storage_volumes):
        """Make storage volumes data dictionary"""
        vols = []
        for vol in storage_volumes:
            volume = {'properties': {'name': vol['name'], 'description': 'non-boot private volume',
                                     'storagePool': vol['storagePool'],
                                     'size': 35073741824, 'provisioningType': 'Thin',
                                     'isShareable': vol['isShareable']},
                      'templateUri': vol['templateUri'], 'isPermanent': True}
            if 'snapshotPool' in vol:
                volume['properties']['snapshotPool'] = vol['snapshotPool']
            if 'dataProtectionLevel' in vol:
                volume['properties']['dataProtectionLevel'] = vol['dataProtectionLevel']
            if 'provisioningType' in vol:
                volume['properties']['provisioningType'] = vol['provisioningType']
            vols.append(volume)
        return vols

    def existing_storage_volumes(self, storage_volumes):
        """Append storage volume attributes to existing volumes """
        vol = []
        for vols in storage_volumes:
            vol.append({'storageSystemUri': vols['storageSystemUri'], 'deviceVolumeName': vols['name'],
                        'name': vols['name'], 'isShareable': vols['isShareable']})
        return vol

    def expected_storage_volumes(self, storage_volumes):
        """Make expected storage volumes data dictionary"""
        expected_vol = []
        for exp_vols in storage_volumes:
            expected_vol.append(
                {'type': 'StorageVolumeV6', 'name': exp_vols['name'], 'status': 'OK', 'state': 'Managed'})
        return expected_vol

    def make_enclosure_data(self, encls, spp):
        """Make enclosure data dictionary"""
        ret = []
        if spp is None:
            firmware_baseline_uri = None
        else:
            firmware_baseline_uri = '/rest/firmware-drivers/' + spp
        for encl in encls:
            ret.append(
                {'enclosureGroupUri': encl['enclosureGroupUri'], 'hostname': encl['hostname'], 'name': encl['name'],
                 'username': encl['username'], 'password': encl['password'], 'licensingIntent': encl['licensingIntent'],
                 'firmwareBaselineUri': firmware_baseline_uri, 'updateFirmwareOn': encl['updateFirmwareOn'],
                 'forceInstallFirmware': encl['forceInstallFirmware'], 'force': encl['force']})
        return ret

    def make_expected_enclousre_data(self, encls, spp):
        """Make expected enclosure data dictionary"""
        ret = []
        if spp is None:
            firmware_baseline_uri = None
        else:
            firmware_baseline_uri = '/rest/firmware-drivers/' + spp
        for encl in encls:
            ret.append({'type': 'EnclosureV7', 'name': encl['name'], 'state': 'Managed',
                        'fwBaselineUri': firmware_baseline_uri,
                        'logicalEnclosureUri': 'LE:' + encl['name']})
        return ret

    def make_expected_server_profile_data(self, sps, spp, firmware):
        """Make expected server profile data dictionary"""
        ret = []
        if firmware['manageFirmware']:
            firmware_baseline_uri = '/rest/firmware-drivers/' + spp
        else:
            firmware_baseline_uri = None
        for sp in sps:
            local_storage = sp['localStorage']
            if local_storage:
                local_storage['controllers'][0]['initialize'] = False
                local_storage['controllers'][0]['importConfiguration'] = False
                if local_storage['sasLogicalJBODs']:
                    for remove_data in local_storage['sasLogicalJBODs']:
                        del remove_data['numPhysicalDrives'], remove_data['sasLogicalJBODUri']
            if sp['sanStorage']:
                vol_attachement = sp['sanStorage']['volumeAttachments']
                for san in vol_attachement:
                    if san['volumeUri'] is not None:
                        del san['lun'], san['lunType']
                    elif san['volumeUri'] is None:
                        san['volumeUri'] = 'SVOL:' + \
                            san['volume']['properties']['name']
                        del san['lunType'], san['lun'], san['volume']
            if sp['bootMode']:
                ret.append(
                    {'name': sp['name'], 'type': 'ServerProfileV9', 'serverHardwareUri': "SH:" + sp['serverHardwareUri'],
                     'enclosureGroupUri': sp['enclosureGroupUri'],
                     'firmware': {'firmwareInstallType': firmware['firmwareInstallType'],
                                  'manageFirmware': firmware['manageFirmware'],
                                  'firmwareBaselineUri': firmware_baseline_uri},
                     'connectionSettings': sp['connectionSettings'], 'status': 'OK', 'state': 'Normal',
                     'bootMode': sp['bootMode'], 'bios': sp['bios'],
                     'localStorage': local_storage, 'sanStorage': sp['sanStorage']
                     })
            else:
                ret.append(
                    {'name': sp['name'], 'type': 'ServerProfileV9', 'serverHardwareUri': "SH:" + sp['serverHardwareUri'],
                     'enclosureGroupUri': sp['enclosureGroupUri'],
                     'firmware': {'firmwareInstallType': firmware['firmwareInstallType'],
                                  'manageFirmware': firmware['manageFirmware'],
                                  'firmwareBaselineUri': firmware_baseline_uri},
                     'connectionSettings': sp['connectionSettings'], 'status': 'OK', 'state': 'Normal',
                     'bios': sp['bios'],
                     'localStorage': local_storage, 'sanStorage': sp['sanStorage']
                     })
        return ret

    def make_expected_server_profile_from_spt_data(self, sps):
        """Make expected server profile from server profile template data dictionary"""
        ret = []
        for sp in sps:
            ret.append({'type': 'ServerProfileV7', 'serverHardwareUri': 'SH:' + sp['serverHardwareUri'],
                        'name': sp['name'], 'status': 'OK', 'state': 'Normal'})
        return ret

    def make_expected_server_profile_template_data(self, sps, firmware):
        """Make expected server profile template data dictionary"""
        ret = []
        for sp in sps:
            if sp['sanStorage']:
                vol_attachement = sp['sanStorage']['volumeAttachments']
                for san in vol_attachement:
                    if san['volumeUri'] is not None:
                        del san['lun'], san['lunType']
                    elif san['volumeUri'] is None:
                        del san['volumeUri'], san['lunType'], san['lun'], san['volume']['properties']['name']
                        del san['volume']['properties']['isShareable'], san['volume']['properties']['size']
                        del san['volume']['properties']['provisioningType'], san['volume']['isPermanent']
                        del san['volume']['templateUri']
            ret.append({
                "type": "ServerProfileTemplateV5",
                "name": sp['name'],
                "serverHardwareTypeUri": sp['serverHardwareTypeUri'],
                "enclosureGroupUri": sp['enclosureGroupUri'],
                "hideUnusedFlexNics": sp['hideUnusedFlexNics'] if "hideUnusedFlexNics" in sp else False,
                'connectionSettings': sp['connectionSettings'],
                'firmware': {
                    'manageFirmware': firmware['manageFirmware']},
                "sanStorage": sp['sanStorage']
            })
        return ret

    def extract_spp_version(self, spp_name):
        """Extract spp version from spp name"""
        match = re.match(r"SPP(\d\d\d\d)(\d\d)(\d)\.", spp_name)
        if match:
            version = match.groups()
            return version[0] + "." + version[1] + "." + version[2]
#        else:
#            raise Exception("Unable to extract SPP version. Please specify SPP version explicitly")
