import inspect
import acitoolkit.acitoolkit as ACI
from RoboGalaxyLibrary.utilitylib import logging as logger
import re
import time
from acitoolkit.acibaseobject import BaseACIObject
from acitoolkit import Session, Tenant, Credentials, BaseACIObject, BridgeDomain, AppProfile, EPG
from acitoolkit.acitoolkit import Interface, PortChannel, Tenant, AppProfile, L2Interface, EPG, Context


class APICOperations:

    def _get_my_method(self):
        frame = inspect.stack()[1]
        module = inspect.getframeinfo(frame[0])
        return module.function

    def _check_and_update_vlan_range_type(self, vlanRange):
        if isinstance(vlanRange, dict):
            vlanRangeList = []
            vlanRangeList.append(vlanRange)
        elif isinstance(vlanRange, list):
            vlanRangeList = vlanRange
        else:
            error = ['%% ERROR:%s.%s:Invalid data type for vlanRange: %s!' % (self.__class__.__name__, self._get_my_method(), type(vlanRange))]
            error += re.findall("text\":\"(.*)\"", res.content)
            raise Exception(" ".join(error))
        return vlanRangeList

    def get_apic_session(self, url, username, password):
        apic_session = ACI.Session(url, username, password)
        res = apic_session.login()
        if not res.ok:
            error = ['%% ERROR:%s.%s:Could not login to APIC!' % (self.__class__.__name__, self._get_my_method())]
            error += re.findall("text\":\"(.*)\"", res.content)
            raise Exception(" ".join(error))
        return apic_session

    def push_configuration(self, session, url, data):
        resp = session.push_to_apic(url, data)
        if not resp.ok:
            logger._log('%% Error:%s.%s:Could not push configuration to APIC!' % (self.__class__.__name__, self._get_my_method()))
            logger._log(resp.text)
            return False
        else:
            return True

#
# class TenantOperations(APICOperations):
#
    def create_tenant(self, session, tenants):
        for t in tenants:
            logger._log('Creating Tenant: {}'.format(t))
            tenantObj = ACI.Tenant(t)
            resp = session.push_to_apic(tenantObj.get_url(), tenantObj.get_json())
            if not resp.ok:
                logger._log('%% Error:%s.%s:Could not push configuration to APIC!' % (self.__class__.__name__, self._get_my_method()))
                logger._log(resp.text)

    def create_epgs(self, session, tenant, profile, vrf, epgs):
        tenantObj = Tenant(tenant)
        profileObj = AppProfile(profile, tenantObj)
        logger._log('Creating VRF: {}'.format(vrf))
        vrfObj = Context(vrf, tenantObj)

        vlanRangeList = self._check_and_update_vlan_range_type(epgs['bridgeDomain']['vlanRange'])
        for r in vlanRangeList:
            for vlanId in xrange(r['start'], r['end'] + 1):
                logger._log('Creating Bridge Domain: {}'.format(epgs['bridgeDomain']['namePrefix'] + str(vlanId)))
                bridgeDomainObj = BridgeDomain(epgs['bridgeDomain']['namePrefix'] + str(vlanId), tenantObj)
                logger._log('Selecting VRF \"{}\" in Bridge Domain.'.format(vrf))
                bridgeDomainObj.add_context(vrfObj)
                if epgs['bridgeDomain']['subnetIPv4Addr'] is None:
                    bridgeDomainObj.set_arp_flood(epgs['bridgeDomain']['arpFlood']) if epgs['bridgeDomain']['arpFlood'] else bridgeDomainObj.set_arp_flood('yes')
                    bridgeDomainObj.set_unicast_route('no')
                else:
                    if epgs['bridgeDomain']['arpFlood'] is not None:
                        bridgeDomainObj.set_arp_flood(epgs['bridgeDomain']['arpFlood'])
                    else:
                        bridgeDomainObj.set_arp_flood('no')
                    bridgeDomainObj.set_unicast_route('yes')
                    subnet = Subnet('', bridgeDomainObj)
                    subnet.addr = epgs['bridgeDomain']['subnetIPv4Addr']
                    if epgs['bridgeDomain']['scope'] is None:
                        subnet.set_scope("private")
                    else:
                        subnet.set_scope(epgs['bridgeDomain']['scope'])
                bridgeDomainObj.set_unknown_mac_unicast(epgs['bridgeDomain']['unkMacUcastAct'])

                logger._log('Creating EPG: {}'.format(epgs['namePrefix'] + str(vlanId)))
                epg = EPG(epgs['namePrefix'] + str(vlanId), profileObj)
                # Place EPG in the Bridge Domain
                logger._log('Selecting Bridge Domain \"{}\" in EPG.\n'.format(epgs['bridgeDomain']['namePrefix'] + str(vlanId)))
                epg.add_bd(bridgeDomainObj)

                resp = session.push_to_apic(tenantObj.get_url(),
                                            tenantObj.get_json())

                if not resp.ok:
                    logger._log('%% Error:%s.%s:Could not push configuration to APIC!' % (self.__class__.__name__, self._get_my_method()))
                    logger._log(resp.text)

    def create_bridge_domains(self, session, tenant, vrf, bridgeDomains):
        tenantObj = Tenant(tenant)
        vrfObj = Context(vrf, tenantObj)

        for bd in bridgeDomains:
            print("DEBUG: bd=%s" % bd)
            vlanRangeList = self._check_and_update_vlan_range_type(bd['vlanRange'])
            for r in vlanRangeList:
                for vlanId in xrange(r['start'], r['end'] + 1):
                    bridgeDomainObj = BridgeDomain(bd['namePrefix'] + str(vlanId), tenantObj)
                    bridgeDomainObj.add_context(vrfObj)
                    if bd['subnetIPv4Addr'] is None:
                        bridgeDomainObj.set_arp_flood(bd['arpFlood']) if bd['arpFlood'] else bridgeDomainObj.set_arp_flood('yes')
                        bridgeDomainObj.set_unicast_route('no')
                    else:
                        if bd['arpFlood'] is not None:
                            bridgeDomainObj.set_arp_flood(bd['arpFlood'])
                        else:
                            bridgeDomainObj.set_arp_flood('no')
                        bridgeDomainObj.set_unicast_route('yes')
                        subnet = Subnet('', bridgeDomainObj)
                        subnet.addr = bd['subnetIPv4Addr']
                        if bd['scope'] is None:
                            subnet.set_scope("private")
                        else:
                            subnet.set_scope(bd['scope'])
                    bridgeDomainObj.set_unknown_mac_unicast(bd['unkMacUcastAct'])
                    logger._log('Creating Bridge Domain: {}'.format(bd['namePrefix'] + str(vlanId)))
                    resp = session.push_to_apic(tenantObj.get_url(),
                                                tenantObj.get_json())
                    if not resp.ok:
                        logger._log('%% Error:%s.%s:Could not push configuration to APIC!' % (self.__class__.__name__, self._get_my_method()))
                        logger._log(resp.text)

    def build_static_ports_to_epg_payload(self, vlan, pod, node, path, urgency='immediate', mode='regular'):
        staticPortsPayload = {}
        fvRsPathAtt = {}
        attributes = {}
        attributes["encap"] = "vlan-{}".format(vlan)
        attributes["instrImedcy"] = urgency
        attributes["mode"] = mode
        attributes["tDn"] = "topology/pod-{}/{}/pathep-[{}]".format(pod, node, path)
        attributes["status"] = "created"
        fvRsPathAtt["attributes"] = attributes
        fvRsPathAtt["children"] = []
        staticPortsPayload["fvRsPathAtt"] = fvRsPathAtt

        return staticPortsPayload

    def build_domain_association_payload(self, domain, urgency='immediate'):
        tDn = {"phys": "uni/%s-%s" % (domain['type'], domain['profile']), "vmmp": "uni/%s-%s/dom-%s" % (domain['type'], domain.get('vmType'), domain['profile'])}
        domainPayload = {}
        fvRsDomAtt = {}
        attributes = {}
        attributes["resImedcy"] = urgency
        attributes["tDn"] = tDn[domain['type']]
        attributes["status"] = "created"
        fvRsDomAtt["attributes"] = attributes
        fvRsDomAtt["children"] = []
        domainPayload["fvRsDomAtt"] = fvRsDomAtt

        return domainPayload

    def attach_epg_to_vlan(self, session, tenant, profile, vrf, epgs):
        tenantObj = Tenant(tenant)
        profileObj = AppProfile(profile, tenantObj)
        vrfObj = Context(vrf, tenantObj)

        vlanRangeList = self._check_and_update_vlan_range_type(epgs['bridgeDomain']['vlanRange'])
        payload = {}
        for r in vlanRangeList:
            for vlanId in xrange(r['start'], r['end'] + 1):
                bridgeDomainObj = BridgeDomain(epgs['bridgeDomain']['namePrefix'] + str(vlanId), tenantObj)
                bridgeDomainObj.add_context(vrfObj)
                epgObj = EPG(epgs['bridgeDomain']['namePrefix'] + str(vlanId), profileObj)
                # Place EPG in the Bridge Domain
                epgObj.add_bd(bridgeDomainObj)
                for s in epgs['staticPorts']:
                    payload = self.build_static_ports_to_epg_payload(vlanId, s['pod'], s['node'], s['path'])
                    url = "/api/node/mo/uni/tn-" + tenant + "/ap-" + profile + "/epg-" + epgs['namePrefix'] + str(vlanId) + ".json"
                    logger._log('Attach EPG \"{}\" to VLAN.'.format(epgs['namePrefix'] + str(vlanId)))
                    self.push_configuration(session, url, payload)
                if epgs['domain'] is not None:
                    logger._log("Associate physical domain \"%s\" to EPG \"%s\".\n" % (epgs['domain'], format(epgs['namePrefix'] + str(vlanId))))
                    payload = self.build_domain_association_payload(epgs['domain'])
                    self.push_configuration(session, url, payload)

    def delete_tenant(self, session, tenant):
        tenantsObj = Tenant.get(session)
        for t in tenantsObj:
            if str(t) == tenant:
                logger._log('DEBUG: Tenant Found: {}'.format(t))
                t.mark_as_deleted()
                # logger._log('DEBUG: request payload/get_json(): {}'.format(t.get_json()))
                resp = t.push_to_apic(session)
                if resp.ok:
                    logger._log('Deleted tenant: {}'.format(t.name))
                else:
                    logger._log('%% ERROR:%s.%s:Delete Tenant failed: %s' % (self.__class__.__name__, self._get_my_method(), t.name))
                    logger._log(resp.text)

    def delete_application_profile(self, session, tenant, profile):
        tenantsObj = ACI.Tenant.get(session)
        tflg = False
        appflg = False
        domainflg = False
        for t in tenantsObj:
            if str(t) == tenant:
                logger._log('DEBUG: Tenant Found: {}'.format(t))
                tflg = True
                profilesObj = ACI.AppProfile.get(session, t)
                for p in profilesObj:
                    if str(p) == profile:
                        logger._log('DEBUG: Application Profile Found: {}'.format(p))
                        appflg = True
                        p.mark_as_deleted()
                        # logger._log('DEBUG: request payload/get_json(): {}'.format(t.get_json()))
                        resp = t.push_to_apic(session)
                        if resp.ok:
                            logger._log('Deleted Application Profile: {}'.format(p))
                        else:
                            logger._log('%% ERROR:%s.%s:Delete Application Profile failed: %s' % (self.__class__.__name__, self._get_my_method(), p))
                            logger._log(resp.text)
                        break
        if tflg:
            if not appflg:
                logger._log('%% WARN:%s.%s:Application Profile not found: %s' % (self.__class__.__name__, self._get_my_method(), profile))
        else:
            logger._log('%% WARN:%s.%s:Tenant not found: %s' % (self.__class__.__name__, self._get_my_method(), tenant))

    def delete_epgs(self, session, tenant, profile, epgs):
        tenantsObj = ACI.Tenant.get(session)
        for t in tenantsObj:
            if str(t) == tenant:
                logger._log('DEBUG: Tenant Found: {}'.format(t))
                profilesObj = ACI.AppProfile.get(session, t)
                for p in profilesObj:
                    if str(p) == profile:
                        logger._log('DEBUG: Application Profile Found: {}'.format(p))
                        epgsObj = ACI.EPG.get(session, p, t)
                        for e in epgs:
                            vlanRangeList = self._check_and_update_vlan_range_type(e['bridgeDomain']['vlanRange'])
                            for r in vlanRangeList:
                                for vlanId in xrange(r['start'], r['end'] + 1):
                                    found = False
                                    for eO in epgsObj:
                                        if str(e['namePrefix']) + str(vlanId) == str(eO):
                                            logger._log('DEBUG: Marking {} for deletion...'.format(str(e['namePrefix']) + str(vlanId)))
                                            found = True
                                            eO.mark_as_deleted()
                                    if not found:
                                        logger._log('%% WARN:%s.%s:EPG Not Found: %s' % (self.__class__.__name__, self._get_my_method(), str(e['namePrefix']) + str(vlanId)))
                # logger._log('DEBUG: request payload/get_json(): {}'.format(t.get_json()))
                resp = t.push_to_apic(session)
                if resp.ok:
                    logger._log('Deleted marked EPG(s).')
                else:
                    logger._log('%% ERROR:%s.%s:Delete of marked EPG(s) failed.' % (self.__class__.__name__, self._get_my_method()))
                    logger._log(resp.text)

    def delete_bridge_domains(self, session, tenant, bridgeDomains):
        tenantsObj = ACI.Tenant.get(session)
        for t in tenantsObj:
            if str(t) == tenant:
                logger._log('DEBUG: Tenant Found: {}'.format(t))
                bridgeDomainsObj = ACI.BridgeDomain.get(session, t)
                for b in bridgeDomainsObj:
                    vlanRangeList = self._check_and_update_vlan_range_type(bridgeDomains['vlanRange'])
                    for r in vlanRangeList:
                        for vlanId in xrange(r['start'], r['end'] + 1):
                            found = False
                            if str(bridgeDomains['namePrefix']) + str(vlanId) == str(b):
                                logger._log('DEBUG: Marking Bridge Domain {} for deletion...'.format(str(bridgeDomains['namePrefix']) + str(vlanId)))
                                found = True
                                b.mark_as_deleted()
                                if not found:
                                    logger._log('%% WARN:%s.%s:Bridge Domain Not Found: %s' % (self.__class__.__name__, self._get_my_method(), str(bridgeDomains['namePrefix']) + str(vlanId)))
                # logger._log('DEBUG: request payload/get_json(): {}'.format(t.get_json()))
                resp = t.push_to_apic(session)
                if resp.ok:
                    logger._log('Deleted marked Bridge Domain(s).')
                else:
                    logger._log('%% ERROR:%s.%s:Delete of marked Bridge Domain(s) failed.' % (self.__class__.__name__, self._get_my_method()))
                    logger._log(resp.text)

    def delete_vrf(self, session, tenant, vrf):
        tenantsObj = ACI.Tenant.get(session)
        for t in tenantsObj:
            if str(t) == tenant:
                logger._log('DEBUG: Tenant Found: {}'.format(t))
                vrfsObj = ACI.Context.get(session, t)
                found = False
                for v in vrfsObj:
                    if str(v) == vrf:
                        logger._log('DEBUG: Marking VRF {} for deletion...'.format(str(v)))
                        found = True
                        v.mark_as_deleted()
                if not found:
                    logger._log('%% WARN:%s.%s:VRF Not Found: %s' % (self.__class__.__name__, self._get_my_method(), str(v)))
                # logger._log('DEBUG: request payload/get_json(): {}'.format(t.get_json()))
                resp = t.push_to_apic(session)
                if resp.ok:
                    logger._log('Deleted marked Bridge Domain(s).')
                else:
                    logger._log('%% ERROR:%s.%s:Delete of marked Bridge Domain(s) failed.' % (self.__class__.__name__, self._get_my_method()))
                    logger._log(resp.text)

#
# class FabricOperations(APICOperations):
#
    def create_vlan_pool(self, session, vlanPool):
        """
           Create VLAN Pool
            Arguments:
            session - APIC session object
            vlanPool - dictionary of VLAN Pool data
        """
        payload_children = []
        for r in vlanPool['ranges']:
            from_id = vlanPool['encapType'] + '-' + r['startVlan']
            to_id = vlanPool['encapType'] + '-' + r['endVlan']
            fvnsEncapBlk = {'fvnsEncapBlk': {'attributes': {'name': 'encap',
                                                            'from': from_id,
                                                            'to': to_id},
                                             'children': []}}
            if r.get('allocMode') is not None:
                fvnsEncapBlk['fvnsEncapBlk']['attributes']['allocMode'] = r['allocMode']
            payload_children.append(fvnsEncapBlk)
        pool_attributes = {'name': vlanPool['name']}
        if vlanPool['encapType'] == 'vlan':
            fvnsEncapInstP_string = 'fvnsVlanInstP'
            pool_attributes['allocMode'] = vlanPool['allocMode']
        elif vlanPool['encapType'] == 'vxlan':
            fvnsEncapInstP_string = 'fvnsVxlanInstP'
        fvnsEncapInstP = {fvnsEncapInstP_string: {'attributes': pool_attributes,
                                                  'children': payload_children}}
        payload = {'infraInfra': {'attributes': {},
                                  'children': [fvnsEncapInstP]}}
        resp = session.push_to_apic("/api/mo/uni/infra.json", payload)
        if not resp.ok:
            logger._log('%% ERROR:%s.%s:Failed to push configuration to APIC.' % (self.__class__.__name__, self._get_my_method()))
            logger._log(vlanresp.text)

    def build_physical_domain_payload(self, physicalDomain):
        physDomP = {}
        physDomPAttributes = {}
        attributes = {}
        attributes["dn"] = "uni/phys-{}".format(physicalDomain['name'])
        attributes["name"] = physicalDomain['name']
        attributes["rn"] = "phys-{}".format(physicalDomain['name'])
        attributes["status"] = "created"
        physDomPAttributes["attributes"] = attributes
        physDomP["physDomP"] = physDomPAttributes

        chldrn = {}
        chldrn["children"] = []
        infraRsVlanNs = {}
        infraRsVlanNs_attributes = {}
        attributes = {}
        attributes["tDn"] = "uni/infra/vlanns-[{}]-static".format(physicalDomain['vlanPool']['name'])
        attributes["status"] = "created"
        infraRsVlanNs_attributes["attributes"] = attributes
        infraRsVlanNs_attributes["children"] = []
        infraRsVlanNs["infraRsVlanNs"] = infraRsVlanNs_attributes
        chldrn["children"].append(infraRsVlanNs)

        physDomP["physDomP"] = physDomPAttributes
        physDomP["physDomP"].update(chldrn)
        return physDomP

    def create_physical_domain(self, session, physicalDomain):
        url = "/api/node/mo/uni/phys-%s.json" % physicalDomain['name']
        payload = self.build_physical_domain_payload(physicalDomain)
        self.push_configuration(session, url, payload)

    def build_physical_domain_children(self, physicalDomainName):
        chldrn = {}
        chldrn["children"] = []
        infraEntP = {}
        infraRsDomP = {}
        attributes = {}
        attributes["tDn"] = "uni/phys-{}".format(physicalDomainName)
        attributes["status"] = "created"
        infraRsDomP["attributes"] = attributes
        infraRsDomP["children"] = []
        infraEntP["infraRsDomP"] = infraRsDomP
        chldrn["children"].append(infraEntP)
        return chldrn

    def build_attachable_access_entity_profile_payload(self, aaepName, physicalDomainName):
        """
           Build Attachable Access Entity Profile payload
               Arguments:
               aaepName - an Attachable Access Entity Profile name
               physicalDomainName - a name of Physical Domain you want the AEP to be attached
        """
        infrainfra = {}
        infrattributes = {}
        attributes = {}
        attributes["dn"] = "uni/infra"
        attributes["status"] = "modified"
        infrattributes["attributes"] = attributes
        infrainfra["infraInfra"] = infrattributes

        childrn = {}
        childrn["children"] = []

        infraEntP = {}
        infraAttEntityP = {}
        attributes = {}
        attributes["dn"] = "uni/infra/attentp-{}".format(aaepName)
        attributes["name"] = aaepName
        attributes["rn"] = "attentp-{}".format(aaepName)
        attributes["status"] = "created"
        infraAttEntityP["attributes"] = attributes
        infraEntP['infraAttEntityP'] = infraAttEntityP
        infraEntP['infraAttEntityP'].update(self.build_physical_domain_children(physicalDomainName))
        childrn["children"].append(infraEntP)

        infrafunk = {}
        infraattributes = {}
        attributes = {}
        attributes["dn"] = "uni/infra/funcprof"
        attributes["status"] = "modified"
        infraattributes["attributes"] = attributes
        infraattributes["children"] = []
        infrafunk["infraFuncP"] = infraattributes
        childrn["children"].append(infrafunk)
        infrainfra["infraInfra"].update(childrn)
        return infrainfra

    def create_attachable_access_entity_profile(self, session, attachableAEP):
        """
           Create Attachable Access Entity Profile in APIC Fabric Access Policies
            Arguments:
            session - APIC session object
            attachableAEP - a dictionary of Attachable Access Entity Profile defined in your data variable file
        """
        url = "/api/node/mo/uni/infra.json"
        payload = self.build_attachable_access_entity_profile_payload(attachableAEP['name'], attachableAEP['physicalDomain'])
        self.push_configuration(session, url, payload)

    def build_access_port_policy_group_payload(self, accessPortPolicy):
        payload = {}
        infraAccPortGrp = {}
        attributes = {}
        infraAccPortGrp["dn"] = "uni/infra/funcprof/accportgrp-{}".format(accessPortPolicy['name'])
        infraAccPortGrp["name"] = accessPortPolicy['name']
        infraAccPortGrp["rn"] = "accportgrp-{}".format(accessPortPolicy['name'])
        infraAccPortGrp["status"] = "created"
        attributes["attributes"] = infraAccPortGrp
        payload["infraAccPortGrp"] = attributes

        chldrn = {}
        chldrn["children"] = []

        infraEntP = {}
        infraRsAttEntP = {}
        attributes = {}
        attributes["tDn"] = "uni/infra/attentp-{}".format(accessPortPolicy['aepName'])
        attributes["status"] = "created,modified"
        infraRsAttEntP["attributes"] = attributes
        infraRsAttEntP["children"] = []
        infraEntP["infraRsAttEntP"] = infraRsAttEntP

        infraCDP = {}
        infraRsCdpIfPol = {}
        attributes = {}
        attributes["tnCdpIfPolName"] = accessPortPolicy['cdpPolicy']
        attributes["status"] = "created,modified"
        infraRsCdpIfPol["attributes"] = attributes
        infraRsCdpIfPol["children"] = []
        infraCDP['infraRsCdpIfPol'] = infraRsCdpIfPol

        infraLLDP = {}
        infraRsLldpIfPol = {}
        attributes = {}
        attributes["tnLldpIfPolName"] = accessPortPolicy['lldpPolicy']
        attributes["status"] = "created,modified"
        infraRsLldpIfPol["attributes"] = attributes
        infraRsLldpIfPol["children"] = []
        infraLLDP['infraRsLldpIfPol'] = infraRsLldpIfPol

        infraL2 = {}
        infraRsL2IfPol = {}
        attributes = {}
        attributes["tnL2IfPolName"] = accessPortPolicy['l2Policy']
        attributes["status"] = "created,modified"
        infraRsL2IfPol["attributes"] = attributes
        infraRsL2IfPol["children"] = []
        infraL2['infraRsL2IfPol'] = infraRsL2IfPol

        chldrn["children"].append(infraEntP)
        chldrn["children"].append(infraCDP)
        chldrn["children"].append(infraLLDP)
        chldrn["children"].append(infraL2)
        payload['infraAccPortGrp'].update(chldrn)

        return payload

    def build_vpc_policy_group_payload(self, vpcPolicy):
        payload = {}
        infraAccBndlGrp = {}
        attributes = {}
        infraAccBndlGrp["dn"] = "uni/infra/funcprof/accbundle-{}".format(vpcPolicy['name'])
        infraAccBndlGrp["name"] = vpcPolicy['name']
        infraAccBndlGrp["lagT"] = "node"
        infraAccBndlGrp["rn"] = "accbundle-{}".format(vpcPolicy['name'])
        infraAccBndlGrp["status"] = "created"
        attributes["attributes"] = infraAccBndlGrp
        payload["infraAccBndlGrp"] = attributes

        chldrn = {}
        chldrn["children"] = []

        infraEntP = {}
        infraRsAttEntP = {}
        attributes = {}
        attributes["tDn"] = "uni/infra/attentp-{}".format(vpcPolicy['aepName'])
        attributes["status"] = "created,modified"
        infraRsAttEntP["attributes"] = attributes
        infraRsAttEntP["children"] = []
        infraEntP["infraRsAttEntP"] = infraRsAttEntP

        infraCDP = {}
        infraRsCdpIfPol = {}
        attributes = {}
        attributes["tnCdpIfPolName"] = vpcPolicy['cdpPolicy']
        attributes["status"] = "created,modified"
        infraRsCdpIfPol["attributes"] = attributes
        infraRsCdpIfPol["children"] = []
        infraCDP['infraRsCdpIfPol'] = infraRsCdpIfPol

        infraLLDP = {}
        infraRsLldpIfPol = {}
        attributes = {}
        attributes["tnLldpIfPolName"] = vpcPolicy['lldpPolicy']
        attributes["status"] = "created,modified"
        infraRsLldpIfPol["attributes"] = attributes
        infraRsLldpIfPol["children"] = []
        infraLLDP['infraRsLldpIfPol'] = infraRsLldpIfPol

        infraL2 = {}
        infraRsL2IfPol = {}
        attributes = {}
        attributes["tnL2IfPolName"] = vpcPolicy['l2Policy']
        attributes["status"] = "created,modified"
        infraRsL2IfPol["attributes"] = attributes
        infraRsL2IfPol["children"] = []
        infraL2['infraRsL2IfPol'] = infraRsL2IfPol

        infraLacp = {}
        infraRsLacpPol = {}
        attributes = {}
        attributes["tnLacpLagPolName"] = vpcPolicy['lacpLagPolicy']
        attributes["status"] = "created,modified"
        infraRsLacpPol["attributes"] = attributes
        infraRsLacpPol["children"] = []
        infraLacp['infraRsLacpPol'] = infraRsLacpPol

        chldrn["children"].append(infraEntP)
        chldrn["children"].append(infraCDP)
        chldrn["children"].append(infraLLDP)
        chldrn["children"].append(infraL2)
        chldrn["children"].append(infraLacp)
        payload['infraAccBndlGrp'].update(chldrn)

        return payload

    def create_access_port_interface_policy_group(self, session, accessPortPolicy):
        """
           Create Access Port Interface Policy Group
            Arguments:
            session - APIC session object
            accessPortPolicy - dictionary of Access Port IPG data defined in your data variable file
        """
        url = "/api/node/mo/uni/infra/funcprof/accportgrp-%s.json" % accessPortPolicy['name']
        payload = self.build_access_port_policy_group_payload(accessPortPolicy)
        self.push_configuration(session, url, payload)

    def create_vpc_interface_policy_group(self, session, vpcPolicy):
        """
           Create Virtual Port Channel Interface Policy Group
            Arguments:
            session - APIC session object
            vpcPolicy - dictionary of vPC IPG data defined in your data variable file
        """
        url = "/api/node/mo/uni/infra/funcprof/accbundle-%s.json" % vpcPolicy['name']
        payload = self.build_vpc_policy_group_payload(vpcPolicy)
        self.push_configuration(session, url, payload)

    def build_leaf_interface_profile_payload(self, leafInterfaceProfile):
        """
           Build Leaf Interface Profile with Access Port Selector payload
           Arguments:
              leafInterfaceProfile - list of dictionary of Leaf Interface Profile data
        """
        policyGroupType = {"vPC": "accbundle", "accessPort": "accportgrp"}
        payload = {}
        infraAccPortP = {}
        attributes = {}
        infraAccPortP["dn"] = "uni/infra/accportprof-%s" % leafInterfaceProfile['name']
        infraAccPortP["name"] = leafInterfaceProfile['name']
        infraAccPortP["rn"] = "accportgrp-%s" % leafInterfaceProfile['name']
        infraAccPortP["status"] = "created"
        attributes["attributes"] = infraAccPortP
        payload["infraAccPortP"] = attributes

        chldrn = {}
        chldrn["children"] = []

        for accessPortSelector in leafInterfaceProfile['accessPortSelector']:
            fosterChld = {}
            infraHPortS = {}
            attributes = {}
            attributes["dn"] = "uni/infra/accportprof-%s/hports-%s-typ-range" % (leafInterfaceProfile['name'], accessPortSelector['name'])
            attributes["name"] = accessPortSelector['name']
            attributes["rn"] = "hports-%s-typ-range" % accessPortSelector['name']
            attributes["status"] = "created,modified"
            infraHPortS["attributes"] = attributes
            infraHPortS["children"] = []
            for iface in accessPortSelector['interfaces']:
                fosterGrandChld = {}
                infraPortBlk = {}
                attributes = {}
                attributes["dn"] = "uni/infra/accportprof-%s/hports-%s-typ-range/portblk-%s" % (leafInterfaceProfile['name'], accessPortSelector['name'], iface['blockName'])
                attributes["fromCard"] = iface["fromCard"]
                attributes["toCard"] = iface["toCard"]
                attributes["fromPort"] = iface["fromPort"]
                attributes["toPort"] = iface["toPort"]
                attributes["name"] = iface["blockName"]
                attributes["rn"] = "portblk-%s" % iface["blockName"]
                attributes["status"] = "created,modified"
                infraPortBlk["attributes"] = attributes
                infraPortBlk["children"] = []
                fosterGrandChld["infraPortBlk"] = infraPortBlk
                infraHPortS["children"].append(fosterGrandChld)

                fosterGrandChld = {}
                infraRsAccBaseGrp = {}
                attributes = {}
                attributes["tDn"] = "uni/infra/funcprof/%s-%s" % (policyGroupType[accessPortSelector['policyGroup']['type']], accessPortSelector['policyGroup']['name'])
                attributes["status"] = "created,modified"
                infraRsAccBaseGrp["attributes"] = attributes
                infraRsAccBaseGrp["children"] = []
                fosterGrandChld["infraRsAccBaseGrp"] = infraRsAccBaseGrp
                infraHPortS["children"].append(fosterGrandChld)

            fosterChld["infraHPortS"] = infraHPortS
            chldrn["children"].append(fosterChld)

        payload["infraAccPortP"].update(chldrn)

        return payload

    def create_leaf_interface_profile(self, session, leafInterfaceProfile):
        """
           Create Leaf Interface Profile
            Arguments:
            session - APIC session object
            leafInterfaceProfile - dictionary of pre-defined Leaf Interface Profiles data
        """
        url = "/api/node/mo/uni/infra/accportprof-%s.json" % leafInterfaceProfile['name']
        payload = self.build_leaf_interface_profile_payload(leafInterfaceProfile)
        self.push_configuration(session, url, payload)

    def build_leaf_profile_payload(self, leafProfile):
        """
           Build Leaf Profile with Leaf Selector payload
           Arguments:
              leafProfile - list of dictionary of Leaf Profile data
        """
        payload = {}
        infraNodeP = {}
        attributes = {}
        infraNodeP["dn"] = "uni/infra/nprof-%s" % leafProfile['name']
        infraNodeP["name"] = leafProfile['name']
        infraNodeP["rn"] = "nprof-%s" % leafProfile['name']
        infraNodeP["status"] = "created,modified"
        attributes["attributes"] = infraNodeP
        payload["infraNodeP"] = attributes

        chldrn = {}
        chldrn["children"] = []

        for leafSelector in leafProfile['leafSelectors']:
            fosterChld = {}
            infraLeafS = {}
            attributes = {}
            attributes["dn"] = "uni/infra/nprof-%s/leaves-%s-typ-range" % (leafProfile['name'], leafSelector['name'])
            attributes["name"] = leafSelector['name']
            attributes["type"] = "range"
            attributes["rn"] = "leaves-%s-typ-range" % leafSelector['name']
            attributes["status"] = "created"
            infraLeafS["attributes"] = attributes
            infraLeafS["children"] = []
            for block in leafSelector['blocks']:
                fosterGrandChld = {}
                infraNodeBlk = {}
                attributes = {}
                attributes["dn"] = "uni/infra/nprof-%s/leaves-%s-typ-range/nodeblk-%s" % (leafProfile['name'], leafSelector['name'], block['name'])
                attributes["from_"] = block["from_"]
                attributes["to_"] = block["to_"]
                attributes["name"] = block["name"]
                attributes["rn"] = "nodeblk-%s" % block["name"]
                attributes["status"] = "created"
                infraNodeBlk["attributes"] = attributes
                infraNodeBlk["children"] = []
                fosterGrandChld["infraNodeBlk"] = infraNodeBlk
                infraLeafS["children"].append(fosterGrandChld)

            fosterChld["infraLeafS"] = infraLeafS
            chldrn["children"].append(fosterChld)

        fosterChld = {}
        infraRsAccPortP = {}
        infraLeafS = {}
        attributes = {}
        attributes["tDn"] = "uni/infra/accportprof-%s" % leafProfile['leafInterfaceProfile']
        attributes["status"] = "created,modified"
        infraRsAccPortP["attributes"] = attributes
        infraRsAccPortP["children"] = []
        fosterChld["infraRsAccPortP"] = infraRsAccPortP
        chldrn["children"].append(fosterChld)

        payload["infraNodeP"].update(chldrn)

        return payload

    def create_leaf_profile(self, session, leafProfile):
        """
           Create Leaf Profile
            Arguments:
            session - APIC session object
            leafProfile - dictionary of pre-defined Leaf Profile data
        """
        url = "/api/node/mo/uni/infra/nprof-%s.json" % leafProfile['name']
        payload = self.build_leaf_profile_payload(leafProfile)
        self.push_configuration(session, url, payload)

    def build_l2_interface_policy_payload(self, l2Interface):
        """
           Build L2 Interface Policy Payload
            Arguments:
            l2Interface - dictionary of pre-defined L2 Interface Policy data
        """
        payload = {}
        l2IfPol = {}
        attributes = {}
        attributes["dn"] = "uni/infra/l2IfP-%s" % l2Interface['name']
        attributes["name"] = l2Interface['name']
        attributes["descr"] = l2Interface['descr']
        attributes["qinq"] = l2Interface['qinq']
        attributes["vepa"] = l2Interface['reflectiveRelay']
        attributes["vlanScope"] = l2Interface['vlanScope']
        attributes["rn"] = "l2IfP-%s" % l2Interface['name']
        attributes["status"] = "created"
        l2IfPol["attributes"] = attributes
        l2IfPol["children"] = []
        payload["l2IfPol"] = l2IfPol

        return payload

    def create_l2_interface_policy(self, session, l2Interface):
        """
           Create L2 Interface Policy
            Arguments:
            session - APIC session object
            l2Interface - dictionary of pre-defined L2 Interface Policy data
        """
        url = "/api/node/mo/uni/infra/l2IfP-%s.json" % l2Interface['name']
        payload = self.build_l2_interface_policy_payload(l2Interface)
        self.push_configuration(session, url, payload)

    def build_lldp_interface_policy_payload(self, lldpInterface):
        """
           Build LLDP Interface Policy Payload
            Arguments:
            lldpInterface - dictionary of pre-defined LLDP Interface Policy data
        """
        payload = {}
        lldpIfPol = {}
        attributes = {}
        attributes["dn"] = "uni/infra/lldpIfP-%s" % lldpInterface['name']
        attributes["name"] = lldpInterface["name"]
        attributes["adminRxSt"] = lldpInterface["adminRxSt"]
        attributes["adminTxSt"] = lldpInterface["adminTxSt"]
        attributes["descr"] = lldpInterface["descr"]
        attributes["nameAlias"] = lldpInterface["nameAlias"]
        attributes["rn"] = "lldpIfP-%s" % lldpInterface['name']
        attributes["status"] = "created"
        lldpIfPol["attributes"] = attributes
        lldpIfPol["children"] = []
        payload["lldpIfPol"] = lldpIfPol

        return payload

    def create_lldp_interface_policy(self, session, lldpInterface):
        """
           Create LLDP Interface Policy
            Arguments:
            session - APIC session object
            lldpInterface - dictionary of pre-defined LLDP Interface Policy data
        """
        url = "/api/node/mo/uni/infra/lldpIfP-%s.json" % lldpInterface['name']
        payload = self.build_lldp_interface_policy_payload(lldpInterface)
        self.push_configuration(session, url, payload)

    def build_cdp_interface_policy_payload(self, cdpInterface):
        """
           Build CDP Interface Policy Payload
            Arguments:
            cdpInterface - dictionary of pre-defined CDP Interface Policy data
        """
        payload = {}
        cdpIfPol = {}
        attributes = {}
        attributes["adminSt"] = cdpInterface["adminSt"]
        attributes["descr"] = cdpInterface["descr"]
        attributes["dn"] = "uni/infra/cdpIfP-%s" % cdpInterface["name"]
        attributes["name"] = cdpInterface["name"]
        attributes["nameAlias"] = cdpInterface["nameAlias"]
        attributes["status"] = "created"
        cdpIfPol["attributes"] = attributes
        cdpIfPol["children"] = []
        payload["cdpIfPol"] = cdpIfPol

        return payload

    def create_cdp_interface_policy(self, session, cdpInterface):
        """
           Build CDP Interface Policy Payload
            Arguments:
            session - APIC session object
            cdpInterface - dictionary of pre-defined CDP Interface Policy data
        """
        url = "/api/node/mo/uni/infra/cdpIfP-%s.json" % cdpInterface["name"]
        payload = self.build_cdp_interface_policy_payload(cdpInterface)
        self.push_configuration(session, url, payload)

    def build_port_channel_interface_policy_payload(self, pcInterface):
        """
           Build Port Channel Interface Policy Payload
            Arguments:
            pcInterface - dictionary of pre-defined Port Channel Interface Policy data
        """
        payload = {}
        lacpLagPol = {}
        attributes = {}
        attributes["dn"] = "uni/infra/lacplagp-%s" % pcInterface["name"]
        attributes["name"] = pcInterface["name"]
        attributes["descr"] = pcInterface["descr"]
        attributes["nameAlias"] = pcInterface["nameAlias"]
        attributes["mode"] = pcInterface["mode"]
        attributes["ctrl"] = pcInterface["ctrl"]
        attributes["minLinks"] = pcInterface["minLinks"]
        attributes["maxLinks"] = pcInterface["maxLinks"]
        attributes["status"] = "created"
        lacpLagPol["attributes"] = attributes
        lacpLagPol["children"] = []
        payload["lacpLagPol"] = lacpLagPol

        return payload

    def create_port_channel_interface_policy(self, session, pcInterface):
        """
           Create Port Channel Interface Policy
            Arguments:
            session - APIC session object
            pcInterface - dictionary of pre-defined Port Channel Interface Policy data
        """
        url = "/api/node/mo/uni/infra/lacplagp-%s.json" % pcInterface["name"]
        payload = self.build_port_channel_interface_policy_payload(pcInterface)
        self.push_configuration(session, url, payload)

#
# class VMNetworkingOperations(APICOperations):
#
    def build_vcenter_domain_payload(self, vCenterDomain):
        """
           Build vCenter Domain Payload
            Arguments:
            vcenterDomain - dictionary of pre-defined vCenter Domain data
        """
        payload = {}
        vmmDomP = {}
        attributes = {}
        attributes["dn"] = "uni/vmmp-VMware/dom-%s" % vCenterDomain["name"]
        attributes["name"] = vCenterDomain["name"]
        attributes["epRetTime"] = vCenterDomain["endPointRetentionTime"]
        attributes["rn"] = "dom-%s" % vCenterDomain["name"]
        attributes["status"] = "created"
        vmmDomP["attributes"] = attributes
        vmmDomP["children"] = []
        # vmmDomP child is vCenterController
        for vcCtrl in vCenterDomain["vCenterController"]:
            vmmCtrlrP = {}
            attributes = {}
            attributes["dn"] = "uni/vmmp-VMware/dom-%s/ctrlr-%s" % (vCenterDomain["name"], vcCtrl["name"])
            attributes["name"] = vcCtrl["name"]
            attributes["hostOrIp"] = vcCtrl["hostOrIp"]
            attributes["dvsVersion"] = vcCtrl["dvsVersion"]
            attributes["rootContName"] = vcCtrl["rootContName"]
            attributes["rn"] = "ctrlr-%s" % vcCtrl["name"]
            attributes["status"] = "created"
            vmmCtrlrP["attributes"] = attributes
            vmmCtrlrP["children"] = []
            # building vmmUsrAccP (child of vmmDomP)
            vmmUsrAccP = {}
            attributes = {}
            attributes["dn"] = "uni/vmmp-VMware/dom-%s/usracc-%s" % (vCenterDomain["name"], vcCtrl["vmmCredential"]["name"])
            attributes["name"] = vcCtrl["vmmCredential"]["name"]
            attributes["descr"] = vcCtrl["vmmCredential"]["descr"]
            attributes["usr"] = vcCtrl["vmmCredential"]["userName"]
            attributes["pwd"] = vcCtrl["vmmCredential"]["password"]
            attributes["rn"] = "usracc-%s" % vcCtrl["vmmCredential"]["name"]
            attributes["status"] = "created"
            vmmUsrAccP["attributes"] = attributes
            vmmUsrAccP["children"] = []
            vmmDomP["children"].append({"vmmUsrAccP": vmmUsrAccP})
            # building vmmCtrlrP child
            vmmRsAcc = {}
            attributes = {}
            attributes["tDn"] = "uni/vmmp-VMware/dom-%s/usracc-%s" % (vCenterDomain["name"], vcCtrl["vmmCredential"]["name"])
            attributes["status"] = "created"
            vmmRsAcc["attributes"] = attributes
            vmmRsAcc["children"] = []
            vmmCtrlrP["children"].append({"vmmRsAcc": vmmRsAcc})
            vmmDomP["children"].append({"vmmCtrlrP": vmmCtrlrP})
        # aaaDomainRef is another child of vmmDomP
        for sd in vCenterDomain["securityDomains"]:
            aaaDomainRef = {}
            attributes = {}
            attributes["dn"] = "uni/vmmp-VMware/dom-%s/domain-%" % (vCenterDomain["name"], sd["name"])
            attributes["name"] = sd["name"]
            attributes["rn"] = "domain-%s" % sd["name"]
            attributes["status"] = "created"
            aaaDomainRef["attributes"] = attributes
            aaaDomainRef["children"] = []
            vmmDomP["children"].append({"aaaDomainRef": aaaDomainRef})
        infraRsVlanNs = {}
        attributes = {}
        attributes["tDn"] = "uni/infra/vlanns-[%s]-%s" % (vCenterDomain["vlanPool"]["name"], vCenterDomain["vlanPool"]["allocMode"])
        attributes["status"] = "created"
        infraRsVlanNs["attributes"] = attributes
        infraRsVlanNs["children"] = []
        vmmDomP["children"].append({"infraRsVlanNs": infraRsVlanNs})
        payload["vmmDomP"] = vmmDomP
        return payload

    def associate_attachable_entity_profile_to_vcenter(self, session, attachableEntityProfile, vCenterDomainName):
        """
           Associate Attachable Entity Profile To vCenter
            Arguments:
            session - APIC session object
            attachableEntityProfile - name of the Attachable Entity Profile
            vCenterDomainName - name of vCenter Domain
        """
        url = "/api/node/mo/uni/infra/attentp-%s.json" % attachableEntityProfile
        payload = {}
        infraRsDomP = {}
        attributes = {}
        attributes["tDn"] = "uni/vmmp-VMware/dom-%s" % vCenterDomainName
        attributes["status"] = "created,modified"
        infraRsDomP["attributes"] = attributes
        infraRsDomP["children"] = []
        payload["infraRsDomP"] = infraRsDomP
        self.push_configuration(session, url, payload)

    def create_vswitch_policies_in_vcenter_domain(self, session, vSwitchPolicies, vCenterDomainName):
        """
           Create vSwitch Policies In vCenter Domain
            Arguments:
            vSwitchPolicies - dictionary of pre-defined vSwitch Policies
            vCenterDomainName - name of the vCenter Domain where the vSwitch Policies be applied
        """
        # set vSwitch Policies
        vSwitchPolicyResolver = {
            "cdpPolicy": {
                "childName": "vmmRsVswitchOverrideCdpIfPol",
                "tDn": "cdpIfP"
            },
            "lldpPolicy": {
                "childName": "vmmRsVswitchOverrideLldpIfPol",
                "tDn": "lldpIfP"
            },
            "portChannelPolicy": {
                "childName": "vmmRsVswitchOverrideLacpPol",
                "tDn": "lacplagp"
            }
        }
        url = "/api/node/mo/uni/vmmp-VMware/dom-%s.json" % vCenterDomainName
        payload = {}
        vmmDomP = {}
        attributes = {}
        attributes["dn"] = "uni/vmmp-VMware/dom-%s" % vCenterDomainName
        attributes["status"] = "modified"
        vmmDomP["attributes"] = attributes
        vmmDomP["children"] = []
        # processing vmmDomP children
        vmmVSwitchPolicyCont = {}
        attributes = {}
        attributes["dn"] = "uni/vmmp-VMware/dom-%s/vswitchpolcont" % vCenterDomainName
        attributes["status"] = "created,modified"
        vmmVSwitchPolicyCont["attributes"] = attributes
        vmmVSwitchPolicyCont["children"] = []
        # processing vmmDomP grandchildren
        for k in vSwitchPolicies.keys():
            chldName = {}
            attributes = {}
            attributes["tDn"] = "uni/infra/%s-%s" % (vSwitchPolicyResolver[k]["tDn"], vSwitchPolicies[k])
            attributes["status"] = "created"
            chldName["attributes"] = attributes
            chldName["children"] = []
            vmmVSwitchPolicyCont["children"].append({vSwitchPolicyResolver[k]["childName"]: chldName})
        vmmDomP["children"].append({"vmmVSwitchPolicyCont": vmmVSwitchPolicyCont})
        payload["vmmDomP"] = vmmDomP
        self.push_configuration(session, url, payload)

    def create_vcenter_domain(self, session, vCenterDomain):
        """
           Create vCenter Domain
            Arguments:
            session - APIC session object
            vcenterDomain - dictionary of pre-defined vCenter Domain data
        """
        url = "/api/node/mo/uni/vmmp-VMware/dom-%s.json" % vCenterDomain["name"]
        payload = self.build_vcenter_domain_payload(vCenterDomain)
        self.push_configuration(session, url, payload)
        self.associate_attachable_entity_profile_to_vcenter(session, vCenterDomain["attachableEntityProfile"], vCenterDomain["name"])
        self.create_vswitch_policies_in_vcenter_domain(session, vCenterDomain["vSwitchPolicies"], vCenterDomain["name"])
