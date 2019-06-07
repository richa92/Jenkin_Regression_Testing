import acitoolkit.acitoolkit as aci
import acitoolkit.acitoolkit as ACI
from RoboGalaxyLibrary.utilitylib import logging as logger
import re
import time
from acitoolkit.acitoolkit import EPG  # Interface, L2Interface, Session.
from acitoolkit.acibaseobject import BaseACIObject
from acitoolkit import Session, Tenant, Credentials, BaseACIObject
from acitoolkit.acitoolkit import Interface, PortChannel, Tenant, AppProfile, L2Interface, EPG


class APICOperations:

    def get_apic_session(self, url, username, password):
        apic_session = aci.Session(url, username, password)
        res = apic_session.login()
        if not res.ok:
            error = ["Could not login to APIC."]
            error += re.findall("text\":\"(.*)\"", res.content)
            raise Exception(" ".join(error))
        return apic_session

    def create_tenant(self, session, tenant_name):
        tenant = aci.Tenant(tenant_name)
        resp = session.push_to_apic(tenant.get_url(), tenant.get_json())
        if not resp.ok:
            logger._log('%% Error: Could not push configuration to APIC')
            logger._log(resp.text)

    def create_tenant_for_scalabilityTest(self, session, numberOfTenants_toBecreated, domain_toBe_attached):
        tenant_Prefix = "FVT_TenantScale_Test"
        app_Profile_name = "FVT_ApPScale_Test"
        epg_name = "FVT_epgScale_Test"
        domainflg = False
        for tenant_no in range(0, int(numberOfTenants_toBecreated)):
            tenant_toBe_created = tenant_Prefix + str(tenant_no)
            appP_toBe_created = app_Profile_name + str(tenant_no)
            epg_toBe_created = epg_name + str(tenant_no)
            tenant = aci.Tenant(tenant_toBe_created)
            app = aci.AppProfile(appP_toBe_created, tenant)
            epg = EPG(epg_toBe_created, app)
            domains = aci.VmmDomain.get(session)
            for domain in domains:
                if str(domain) == domain_toBe_attached:
                    domainflg = True
                    epg.attach(domain)
            if domainflg:
                resp = session.push_to_apic(tenant.get_url(), tenant.get_json())
                time.sleep(1)
                if resp.ok:
                    logger._log("*** {} Tenant Created".format(str(tenant)))
            else:
                logger._log('%% Error: Could not push configuration to APIC')

    def delete_tenant_for_scalabilityTest(self, session):
        tenants = Tenant.get(session)
        for tenant in tenants:
            if re.match("FVT_TenantScale_Test\d+", str(tenant)):
                tenant.mark_as_deleted()
                resp = session.push_to_apic(tenant.get_url(), tenant.get_json())
                if resp.ok:
                    logger._log('***{} Tenant Deleted'.format(str(tenant)))

    def delete_tenant(self, session, tenant_name):
        tenants = Tenant.get(session)
        for tenant in tenants:
            if str(tenant) == tenant_name:
                tenant.mark_as_deleted()
                resp = tenant.push_to_apic(session)
                if resp.ok:
                    logger._log('Deleted tenant', tenant.name)
                else:
                    logger._log('Could not delete tenant', tenant.name)
                    logger._log(resp.text)

    def createApplicationProfile(self, session, user_tenant, app_Profile_name):
        tenants = aci.Tenant.get(session)
        tflg = False
        appflg = False
        domainflg = False
        tenant_available = object
        for tenant in tenants:
            if str(tenant) == user_tenant.strip():
                tenant_available = tenant
                tflg = True
                apps = aci.AppProfile(app_Profile_name, tenant)
        if tflg:
            tenant_available.push_to_apic(session)
        else:
            logger._log("*** {} Tenant is not available in APIC".format(user_tenant))

    def deleteApplicationProfile(self, session, user_tenant, app_Profile_name):
        tenants = aci.Tenant.get(session)
        tflg = False
        appflg = False
        domainflg = False
        tenant_available = object
        for tenant in tenants:
            if str(tenant) == user_tenant.strip():
                tenant_available = tenant
                tflg = True
                apps = aci.AppProfile.get(session, tenant)
                for app in apps:
                    if str(app) == app_Profile_name:
                        appflg = True
                        tenant.mark_as_deleted()
        if tflg:
            tenant_available.push_to_apic(session)
            if not appflg:
                logger._log("*** {} Application Profile is not available in APIC".format(app_Profile_name))
        else:
            logger._log("*** {} Tenant is not available in APIC".format(user_tenant))

    def EPG_creation(self, session, user_tenant, user_appProfile, epg_name_tobe_created):
        tenants = aci.Tenant.get(session)
        tflg = False
        appflg = False
        domainflg = False
        tenant_available = object
        for tenant in tenants:
            if str(tenant) == user_tenant.strip():
                tenant_available = tenant
                tflg = True
                apps = aci.AppProfile.get(session, tenant)
                for app in apps:
                    if str(app) == user_appProfile:
                        appflg = True
                        epg = EPG(epg_name_tobe_created, app)
        if tflg:
            if appflg:
                tenant_available.push_to_apic(session)
            else:
                logger._log("*** {} App Profile is not Available in APIC".format(user_appProfile))
        else:
            logger._log("*** {} Tenant is not available in APIC".format(user_tenant))

    def IntraEPGIsolation_EPG_creation(self, session, user_tenant, user_appProfile, epg_name_tobe_created):
        tenants = aci.Tenant.get(session)
        tflg = False
        appflg = False
        domainflg = False
        tenant_available = object
        for tenant in tenants:
            if str(tenant) == user_tenant.strip():
                tenant_available = tenant
                tflg = True
                apps = aci.AppProfile.get(session, tenant)
                for app in apps:
                    if str(app) == user_appProfile:
                        appflg = True
                        epg = EPG(epg_name_tobe_created, app)
                        epg.set_intra_epg_isolation('enforced')
        if tflg:
            if appflg:
                tenant_available.push_to_apic(session)
            else:
                logger._log("*** {} App Profile is not Available in APIC".format(user_appProfile))
        else:
            logger._log("*** {} Tenant is not available in APIC".format(user_tenant))

    def microSegEPG_creation(self, session, user_tenant, user_appProfile, epg_name_tobe_created):
        tenants = aci.Tenant.get(session)
        tflg = False
        appflg = False
        domainflg = False
        tenant_available = object
        for tenant in tenants:
            if str(tenant) == user_tenant.strip():
                tenant_available = tenant
                tflg = True
                apps = aci.AppProfile.get(session, tenant)
                for app in apps:
                    if str(app) == user_appProfile:
                        appflg = True
                        epg = EPG(epg_name_tobe_created, app)
                        epg.is_attributed_based = True
        if tflg:
            if appflg:
                tenant_available.push_to_apic(session)
            else:
                logger._log("*** {} App Profile is not Available in APIC".format(user_appProfile))
        else:
            logger._log("*** {} Tenant is not available in APIC".format(user_tenant))

    def EPG_creation_and_domainAttch(self, session, user_tenant, user_appProfile, epg_name_tobe_created, user_domain_tobe_attached):
        tenants = aci.Tenant.get(session)
        tflg = False
        appflg = False
        domainflg = False
        tenant_available = object
        for tenant in tenants:
            if str(tenant) == user_tenant:
                tenant_available = tenant
                tflg = True
                apps = aci.AppProfile.get(session, tenant)
                for app in apps:
                    if str(app) == user_appProfile:
                        appflg = True
                        epg = EPG(epg_name_tobe_created, app)
                        domains = aci.VmmDomain.get(session)
                        for domain in domains:
                            if str(domain) == user_domain_tobe_attached:
                                domainflg = True
                                epg.attach(domain)
        if tflg:
            if appflg:
                if domainflg:
                    tenant_available.push_to_apic(session)
                else:
                    logger._log("*** {} VMM domain is not available in APIC".format(user_domain_tobe_attached))
            else:
                logger._log("*** {} App Profile is not Available in APIC".format(user_appProfile))
        else:
            logger._log("*** {} Tenant is not available in APIC".format(user_tenant))

    def ScalingEPG_creation_and_domainAttch(self, session, user_tenant, user_appProfile, user_domain_tobe_attached, number_of_EPG_tobeCreated):
        tenants = aci.Tenant.get(session)
        tflg = False
        appflg = False
        domainflg = False
        tenant_available = object
        for tenant in tenants:
            if str(tenant) == user_tenant:
                tenant_available = tenant
                tflg = True
                apps = aci.AppProfile.get(session, tenant)
                for app in apps:
                    if str(app) == user_appProfile:
                        appflg = True
                        epg_name_string = "FVT_EPGScaling_Test00"
                        for number in range(0, int(number_of_EPG_tobeCreated)):
                            epg_name = epg_name_string + str(number)
                            epg = EPG(epg_name, app)
                            domains = aci.VmmDomain.get(session)
                            for domain in domains:
                                if str(domain) == user_domain_tobe_attached:
                                    domainflg = True
                                    epg.attach(domain)
        if tflg:
            if appflg:
                if domainflg:
                    tenant_available.push_to_apic(session)
                else:
                    logger._log("*** {} VMM domain is not available in APIC".format(user_domain_tobe_attached))
            else:
                logger._log("*** {} App Profile is not Available in APIC".format(user_appProfile))
        else:
            logger._log("*** {} Tenant is not available in APIC".format(user_tenant))

    def ScaleEPG_deletion(self, session):
        tenants = aci.Tenant.get(session)
        for tenant in tenants:
            apps = aci.AppProfile.get(session, tenant)
            for app in apps:
                epgs = aci.EPG.get(session, app, tenant)
                for epg in epgs:
                    if re.match("FVT_EPGScaling_Test00\d+", str(epg)):
                        epg.mark_as_deleted()
                        resp = tenant.push_to_apic(session)
                        if resp.ok:
                            print "Deleted", str(epg)
                        else:
                            print 'Could not delete tenant', str(epg)
                            print resp.text

    def get_Tenant_VLANList(self, session, user_tenant):
        tenants = aci.Tenant.get(session)
        tflg = False
        appflg = False
        epgflg = False
        tenant_available = object
        allepgvlanlist = []
        for tenant in tenants:
            if str(tenant) == user_tenant:
                tenant_available = tenant
                tflg = True
                apps = aci.AppProfile.get(session, tenant)
                for app in apps:
                    appflg = True
                    epgs = aci.EPG.get(session, app, tenant)
                    for epg in epgs:
                        url = "/api/node/mo/uni/epp/fv-[uni/tn-{}/ap-{}/epg-{}].json?query-target=subtree&target-subtree-class=fvIfConn".format(str(tenant), str(app), str(epg))
                        vlanlist = self.get_vlanListForURL(session, url)
                        allepgvlanlist = allepgvlanlist + vlanlist
        return allepgvlanlist

    def get_vlanListForURL(self, session, url):
        response = session.get(url).json()
        imdata = response['imdata']
        objcount = response['totalCount']
        listOfvlans = []
        if objcount > 0:
            for connection in imdata:
                vlanSting = connection["fvIfConn"]["attributes"]["encap"]
                vlan = vlanSting.replace("vlan-", '')
                listOfvlans.append(str(vlan))
        return list(set(listOfvlans))

    def EPG_domainDetach(self, session, user_tenant, user_appProfile, epg_name):
        tenants = aci.Tenant.get(session)
        tflg = False
        appflg = False
        domainflg = False
        epgflg = False
        tenant_available = object
        for tenant in tenants:
            if str(tenant) == user_tenant:
                tenant_available = tenant
                tflg = True
                apps = aci.AppProfile.get(session, tenant)
                for app in apps:
                    if str(app) == user_appProfile:
                        appflg = True
                        #epg = EPG(epg_name_tobe_created,app)
                        epgs = aci.EPG.get(session, app, tenant)
                        for epg in epgs:
                            if str(epg) == epg_name:
                                epgflg = True
                                epg.mark_as_deleted()
        if tflg:
            if appflg:
                if epgflg:
                    tenant_available.push_to_apic(session)
                else:
                    logger._log("*** {} EPG is not available in APIC".format(epg_name))
            else:
                logger._log("*** {} App Profile is not Available in APIC".format(user_appProfile))
        else:
            logger._log("*** {} Tenant is not available in APIC".format(user_tenant))

    # Add_static_binding_interface(self, session, user_tenant, user_appProfile, epg_name, NODE_ID, ENCAP_TYPE, ENCAP_ID,ENCAP_MODE, IMMEDIACY, POD):
    def add_static_binding_interface(self, session, user_tenant, user_appProfile, epg_name, INTERFACE, VLAN):
        # Create the physical interface object
        cong_push = False
        intf = ACI.Interface(INTERFACE['type'], INTERFACE['pod'], INTERFACE['node'], INTERFACE['module'], INTERFACE['port'])
        tenants = aci.Tenant.get(session)
        tflg = False
        appflg = False
        epgflg = False
        tenant_available = object
        epg_available = object
        for tenant in tenants:
            if str(tenant) == user_tenant:
                tenant_available = tenant
                tflg = True
                apps = aci.AppProfile.get(session, tenant)
                for app in apps:
                    if str(app) == user_appProfile:
                        appflg = True
                        epgs = aci.EPG.get(session, app, tenant)
                        for epg in epgs:
                            if str(epg) == epg_name:
                                epgflg = True
                                epg_available = epg
        if tflg:
            if appflg:
                if epgflg:
                    vlan_intf = ACI.L2Interface(VLAN['name'], VLAN['encap_type'], VLAN['encap_id'])
                    vlan_intf.attach(intf)
                    epg_available.attach(vlan_intf)
                    resp = tenant_available.push_to_apic(session)
                    if not resp.ok:
                        logger._log('%% Error: Could not push tenant configuration to APIC')
                        cong_push = False
                    else:
                        cong_push = True
                    # Push the interface attachment to the APIC
                    resp = intf.push_to_apic(session)
                    if not resp.ok:
                        logger._log('%% Error: Could not push interface configuration to APIC')
                else:
                    logger._log("*** {} EPG is not available in APIC".format(epg_name))
            else:
                logger._log("*** {} App Profile is not Available in APIC".format(user_appProfile))
        else:
            logger._log("*** {} Tenant is not available in APIC".format(user_tenant))
        return cong_push

    def remove_static_binding_interface(self, session, user_tenant, user_appProfile, epg_name, INTERFACE, VLAN):
        # Create the physical interface object
        intf = ACI.Interface(INTERFACE['type'], INTERFACE['pod'], INTERFACE['node'], INTERFACE['module'], INTERFACE['port'])
        tenants = aci.Tenant.get(session)
        tflg = False
        appflg = False
        epgflg = False
        tenant_available = object
        epg_available = object
        for tenant in tenants:
            if str(tenant) == user_tenant:
                tenant_available = tenant
                tflg = True
                apps = aci.AppProfile.get(session, tenant)
                for app in apps:
                    if str(app) == user_appProfile:
                        appflg = True
                        epgs = aci.EPG.get(session, app, tenant)
                        for epg in epgs:
                            if str(epg) == epg_name:
                                epgflg = True
                                epg_available = epg
        if tflg:
            if appflg:
                if epgflg:
                    vlan_intf = ACI.L2Interface(VLAN['name'], VLAN['encap_type'], VLAN['encap_id'])
                    vlan_intf.attach(intf)
                    epg_available.detach(vlan_intf)
                    resp = tenant_available.push_to_apic(session)
                    if not resp.ok:
                        logger._log('%% Error: Could not push tenant configuration to APIC')
                    # Push the interface attachment to the APIC
                    resp = intf.push_to_apic(session)
                    if not resp.ok:
                        logger._log('%% Error: Could not push interface configuration to APIC')
                else:
                    logger._log("*** {} EPG is not available in APIC".format(epg_name))
            else:
                logger._log("*** {} App Profile is not Available in APIC".format(user_appProfile))
        else:
            logger._log("*** {} Tenant is not available in APIC".format(user_tenant))

    def add_static_binding_PC(self, session, user_tenant, user_appProfile, epg_name, INTERFACE1, INTERFACE2, PC_VLAN_Details):
        # Create the physical interface objects
        intf1 = Interface(INTERFACE1['type'], INTERFACE1['pod'], INTERFACE1['node'], INTERFACE1['module'], INTERFACE1['port'])
        intf2 = Interface(INTERFACE2['type'], INTERFACE2['pod'], INTERFACE2['node'], INTERFACE2['module'], INTERFACE2['port'])
        # Create a port channel and add physical interfaces
        pc = PortChannel(PC_VLAN_Details['PC_name'])
        pc.attach(intf1)
        pc.attach(intf2)
        vlan_on_pc = L2Interface(PC_VLAN_Details['name'], PC_VLAN_Details['encap_type'], PC_VLAN_Details['encap_id'])
        vlan_on_pc.attach(pc)
        tenants = aci.Tenant.get(session)
        tflg = False
        appflg = False
        epgflg = False
        tenant_available = object
        epg_available = object
        for tenant in tenants:
            if str(tenant) == user_tenant:
                tenant_available = tenant
                tflg = True
                apps = aci.AppProfile.get(session, tenant)
                for app in apps:
                    if str(app) == user_appProfile:
                        appflg = True
                        epgs = aci.EPG.get(session, app, tenant)
                        for epg in epgs:
                            if str(epg) == epg_name:
                                epgflg = True
                                epg_available = epg
        if tflg:
            if appflg:
                if epgflg:
                    epg_available.attach(vlan_on_pc)
                    resp = tenant_available.push_to_apic(session)
                    if not resp.ok:
                        logger._log('%% Error: Could not push tenant configuration to APIC')
                else:
                    logger._log("*** {} EPG is not available in APIC".format(epg_name))
            else:
                logger._log("*** {} App Profile is not Available in APIC".format(user_appProfile))
        else:
            logger._log("*** {} Tenant is not available in APIC".format(user_tenant))

    def remove_static_binding_PC(self, session, user_tenant, user_appProfile, epg_name, INTERFACE1, INTERFACE2, PC_VLAN_Details):
        # Create the physical interface objects
        intf1 = Interface(INTERFACE1['type'], INTERFACE1['pod'], INTERFACE1['node'], INTERFACE1['module'], INTERFACE1['port'])
        intf2 = Interface(INTERFACE2['type'], INTERFACE2['pod'], INTERFACE2['node'], INTERFACE2['module'], INTERFACE2['port'])
        # Create a port channel and add physical interfaces
        pc = PortChannel(PC_VLAN_Details['PC_name'])
        pc.attach(intf1)
        pc.attach(intf2)
        vlan_on_pc = L2Interface(PC_VLAN_Details['name'], PC_VLAN_Details['encap_type'], PC_VLAN_Details['encap_id'])
        vlan_on_pc.attach(pc)
        tenants = aci.Tenant.get(session)
        tflg = False
        appflg = False
        epgflg = False
        tenant_available = object
        epg_available = object
        for tenant in tenants:
            if str(tenant) == user_tenant:
                tenant_available = tenant
                tflg = True
                apps = aci.AppProfile.get(session, tenant)
                for app in apps:
                    if str(app) == user_appProfile:
                        appflg = True
                        epgs = aci.EPG.get(session, app, tenant)
                        for epg in epgs:
                            if str(epg) == epg_name:
                                epgflg = True
                                epg_available = epg
        if tflg:
            if appflg:
                if epgflg:
                    epg_available.detach(vlan_on_pc)
                    resp = tenant_available.push_to_apic(session)
                    if not resp.ok:
                        logger._log('%% Error: Could not push tenant configuration to APIC')
                else:
                    logger._log("*** {} EPG is not available in APIC".format(epg_name))
            else:
                logger._log("*** {} App Profile is not Available in APIC".format(user_appProfile))
        else:
            logger._log("*** {} Tenant is not available in APIC".format(user_tenant))

    def add_static_binding_vPC(self, session, user_tenant, user_appProfile, epg_name, INTERFACE1, INTERFACE2, vPC_VLAN_Details):
        # Create the physical interface objects
        intf1 = Interface(INTERFACE1['type'], INTERFACE1['pod'], INTERFACE1['node'], INTERFACE1['module'], INTERFACE1['port'])
        intf2 = Interface(INTERFACE2['type'], INTERFACE2['pod'], INTERFACE2['node'], INTERFACE2['module'], INTERFACE2['port'])
        # Create a port channel and add physical interfaces
        pc = PortChannel(vPC_VLAN_Details['vPC_name'])
        pc.attach(intf1)
        pc.attach(intf2)
        vlan_on_pc = L2Interface(vPC_VLAN_Details['name'], vPC_VLAN_Details['encap_type'], vPC_VLAN_Details['encap_id'])
        vlan_on_pc.attach(pc)
        tenants = aci.Tenant.get(session)
        tflg = False
        appflg = False
        epgflg = False
        tenant_available = object
        epg_available = object
        for tenant in tenants:
            if str(tenant) == user_tenant:
                tenant_available = tenant
                tflg = True
                apps = aci.AppProfile.get(session, tenant)
                for app in apps:
                    if str(app) == user_appProfile:
                        appflg = True
                        epgs = aci.EPG.get(session, app, tenant)
                        for epg in epgs:
                            if str(epg) == epg_name:
                                epgflg = True
                                epg_available = epg
        if tflg:
            if appflg:
                if epgflg:
                    epg_available.attach(vlan_on_pc)
                    resp = tenant_available.push_to_apic(session)
                    if not resp.ok:
                        logger._log('%% Error: Could not push tenant configuration to APIC')
                else:
                    logger._log("*** {} EPG is not available in APIC".format(epg_name))
            else:
                logger._log("*** {} App Profile is not Available in APIC".format(user_appProfile))
        else:
            logger._log("*** {} Tenant is not available in APIC".format(user_tenant))

    def remove_static_binding_vPC(self, session, user_tenant, user_appProfile, epg_name, INTERFACE1, INTERFACE2, vPC_VLAN_Details):
        # Create the physical interface objects
        intf1 = Interface(INTERFACE1['type'], INTERFACE1['pod'], INTERFACE1['node'], INTERFACE1['module'], INTERFACE1['port'])
        intf2 = Interface(INTERFACE2['type'], INTERFACE2['pod'], INTERFACE2['node'], INTERFACE2['module'], INTERFACE2['port'])
        # Create a port channel and add physical interfaces
        pc = PortChannel(vPC_VLAN_Details['vPC_name'])
        pc.attach(intf1)
        pc.attach(intf2)
        vlan_on_pc = L2Interface(vPC_VLAN_Details['name'], vPC_VLAN_Details['encap_type'], vPC_VLAN_Details['encap_id'])
        vlan_on_pc.attach(pc)
        tenants = aci.Tenant.get(session)
        tflg = False
        appflg = False
        epgflg = False
        tenant_available = object
        epg_available = object
        for tenant in tenants:
            if str(tenant) == user_tenant:
                tenant_available = tenant
                tflg = True
                apps = aci.AppProfile.get(session, tenant)
                for app in apps:
                    if str(app) == user_appProfile:
                        appflg = True
                        epgs = aci.EPG.get(session, app, tenant)
                        for epg in epgs:
                            if str(epg) == epg_name:
                                epgflg = True
                                epg_available = epg
        if tflg:
            if appflg:
                if epgflg:
                    epg.detach(vlan_on_pc)
                    resp = tenant_available.push_to_apic(session)
                    if not resp.ok:
                        logger._log('%% Error: Could not push tenant configuration to APIC')
                else:
                    logger._log("*** {} EPG is not available in APIC".format(epg_name))
            else:
                logger._log("*** {} App Profile is not Available in APIC".format(user_appProfile))
        else:
            logger._log("*** {} Tenant is not available in APIC".format(user_tenant))

    def dynamic_VLAN_pool_creation(self, session, POOL_NAME, ENCAP_TYPE, VLAN_START, VLAN_END):
        vlans = aci.NetworkPool(POOL_NAME, ENCAP_TYPE, VLAN_START, VLAN_END, "dynamic")
        vlanresp = session.push_to_apic(vlans.get_url(), vlans.get_json())
        if not vlanresp.ok:
            logger._log('%% Error: Could not push configuration to APIC')
            logger._log(vlanresp.text)
        return vlans

    def static_VLAN_pool_creation(self, session, POOL_NAME, ENCAP_TYPE, VLAN_START, VLAN_END):
        vlans = aci.NetworkPool(POOL_NAME, ENCAP_TYPE, VLAN_START, VLAN_END, "static")
        vlanresp = session.push_to_apic(vlans.get_url(), vlans.get_json())
        if not vlanresp.ok:
            logger._log('%% Error: Could not push configuration to APIC')
            logger._log(vlanresp.text)

    def Create_VMMDomain(self, session, POOL_NAME, ENCAP_TYPE, VLAN_START, VLAN_END, POOL_MODE, VCENTER_USER, VCENTER_PASS, VMM_TYPE, DATACENTER_NAME, DVS_NAME, VCENTER_IP):
        # Define dynamic vlan range
        vlans = aci.NetworkPool(POOL_NAME, ENCAP_TYPE, VLAN_START, VLAN_END, POOL_MODE)

        # Commit VLAN Range
        vlanresp = session.push_to_apic(vlans.get_url(), vlans.get_json())
        if not vlanresp.ok:
            print('%% Error: Could not push configuration to APIC')
            print(vlanresp.text)

        # Create Credentials object
        vcenter_creds = aci.VMMCredentials(VCENTER_USER, VCENTER_USER, VCENTER_PASS)

        # Vswitch Info object
        vswitch_info = aci.VMMvSwitchInfo(VMM_TYPE, DATACENTER_NAME, DVS_NAME)

        # Create VMM object
        vmm = aci.VMM(DVS_NAME, VCENTER_IP, vcenter_creds, vswitch_info, vlans)
        # Commit Changes
        resp = session.push_to_apic(vmm.get_url(), vmm.get_json())

        if not resp.ok:
            print('%% Error: Could not push configuration to APIC')
            print(resp.text)

    def edit_policyGrp(self, session, url, data):
        vlanresp = session.push_to_apic(url, data)
        if not vlanresp.ok:
            logger._log('%% Error: Could not push configuration to APIC')
            logger._log(vlanresp.text)

    def push_configuration(self, session, url, data):
        resp = session.push_to_apic(url, data)
        if not resp.ok:
            logger._log('%% Error: Could not push configuration to APIC')
            logger._log(resp.text)
            return False
        else:
            return True

    def create_and_edit_cdpIfpol(self, session, url, data):
        resp = session.push_to_apic(url, data)
        if not resp.ok:
            logger._log('%% Error: Could not push configuration to APIC')
            logger._log(resp.text)

    def policygrp_body_build_forCreate(self, portgrp_name, aep_name, cdp_policygrp, lldp_policygrp):
        infraPortGrp = {}
        infraAccPortGrp = {}
        attributes = {}
        infraAccPortGrp["dn"] = "uni/infra/funcprof/accportgrp-{}".format(portgrp_name)
        infraAccPortGrp["name"] = portgrp_name
        infraAccPortGrp["rn"] = "accportgrp-{}".format(portgrp_name)
        infraAccPortGrp["status"] = "created"
        attributes["attributes"] = infraAccPortGrp
        infraPortGrp["infraAccPortGrp"] = attributes

        chldrn = {}
        chldrn["children"] = []

        infraEntP = {}
        infraRsAttEntP = {}
        attributes = {}
        attributes["tDn"] = "uni/infra/attentp-{}".format(aep_name)
        attributes["status"] = "created,modified"
        infraRsAttEntP["attributes"] = attributes
        infraRsAttEntP["children"] = []
        infraEntP["infraRsAttEntP"] = infraRsAttEntP

        infraCDP = {}
        infraRsCdpIfPol = {}
        attributes = {}
        attributes["tnCdpIfPolName"] = cdp_policygrp
        attributes["status"] = "created,modified"
        infraRsCdpIfPol["attributes"] = attributes
        infraRsCdpIfPol["children"] = []
        infraCDP['infraRsCdpIfPol'] = infraRsCdpIfPol

        infraLLDP = {}
        infraRsLldpIfPol = {}
        attributes = {}
        attributes["tnLldpIfPolName"] = lldp_policygrp
        attributes["status"] = "created,modified"
        infraRsLldpIfPol["attributes"] = attributes
        infraRsLldpIfPol["children"] = []
        infraLLDP['infraRsLldpIfPol'] = infraRsLldpIfPol

        chldrn["children"].append(infraEntP)
        chldrn["children"].append(infraCDP)
        chldrn["children"].append(infraLLDP)
        infraPortGrp['infraAccPortGrp'].update(chldrn)

        result = infraPortGrp
        return result

    def policygrp_body_build_forEdit(self, portgrp_name, aep_name, cdp_policygrp, lldp_policygrp):
        infraPortGrp = {}
        infraAccPortGrp = {}
        attributes = {}
        infraAccPortGrp["dn"] = "uni/infra/funcprof/accportgrp-{}".format(portgrp_name)
        infraAccPortGrp["status"] = "modified"
        attributes["attributes"] = infraAccPortGrp
        infraPortGrp["infraAccPortGrp"] = attributes

        chldrn = {}
        chldrn["children"] = []

        infraEntP = {}
        infraRsAttEntP = {}
        attributes = {}
        attributes["tDn"] = "uni/infra/attentp-{}".format(aep_name)
        infraRsAttEntP["attributes"] = attributes
        infraRsAttEntP["children"] = []
        infraEntP["infraRsAttEntP"] = infraRsAttEntP

        infraCDP = {}
        infraRsCdpIfPol = {}
        attributes = {}
        attributes["tnCdpIfPolName"] = cdp_policygrp
        infraRsCdpIfPol["attributes"] = attributes
        infraRsCdpIfPol["children"] = []
        infraCDP['infraRsCdpIfPol'] = infraRsCdpIfPol

        infraLLDP = {}
        infraRsLldpIfPol = {}
        attributes = {}
        attributes["tnLldpIfPolName"] = lldp_policygrp
        infraRsLldpIfPol["attributes"] = attributes
        infraRsLldpIfPol["children"] = []
        infraLLDP['infraRsLldpIfPol'] = infraRsLldpIfPol

        chldrn["children"].append(infraEntP)
        chldrn["children"].append(infraCDP)
        chldrn["children"].append(infraLLDP)
        infraPortGrp['infraAccPortGrp'].update(chldrn)

        result = infraPortGrp
        return result

    def edit_cdpPolicy_AccessPortPolicyGroup(self, policygrp_name, cdpPolicy_name):
        url = "/api/node/mo/uni/infra/funcprof/accportgrp-{}/rscdpIfPol.json".format(policygrp_name)
        infraCDP = {}
        infraRsCdpIfPol = {}
        attributes = {}
        attributes["tnCdpIfPolName"] = cdpPolicy_name
        infraRsCdpIfPol["attributes"] = attributes
        infraRsCdpIfPol["children"] = []
        infraCDP['infraRsCdpIfPol'] = infraRsCdpIfPol
        return infraCDP, url

    def edit_lldpPolicy_AccessPortPolicyGroup(self, policygrp_name, lldpPolicy_name):
        url = "/api/node/mo/uni/infra/funcprof/accportgrp-{}/rslldpIfPol.json".format(policygrp_name)
        infraLLDP = {}
        infraRsLldpIfPol = {}
        attributes = {}
        attributes["tnLldpIfPolName"] = lldpPolicy_name
        infraRsLldpIfPol["attributes"] = attributes
        infraRsLldpIfPol["children"] = []
        infraLLDP['infraRsLldpIfPol'] = infraRsLldpIfPol
        return infraLLDP, url

    def edit_cdppolicy_InPCorvPC_policyGroup(self, policygrp_name, cdpPolicy_name):
        url = "/api/node/mo/uni/infra/funcprof/accbundle-{}/rscdpIfPol.json".format(policygrp_name)
        infraCDP = {}
        infraRsCdpIfPol = {}
        attributes = {}
        attributes["tnCdpIfPolName"] = cdpPolicy_name
        infraRsCdpIfPol["attributes"] = attributes
        infraRsCdpIfPol["children"] = []
        infraCDP['infraRsCdpIfPol'] = infraRsCdpIfPol
        return infraCDP, url

    def edit_lldpPolicy_InPCorvPC_policyGroup(self, policygrp_name, lldpPolicy_name):
        url = "/api/node/mo/uni/infra/funcprof/accbundle-{}/rslldpIfPol.json".format(policygrp_name)
        infraLLDP = {}
        infraRsLldpIfPol = {}
        attributes = {}
        attributes["tnLldpIfPolName"] = lldpPolicy_name
        infraRsLldpIfPol["attributes"] = attributes
        infraRsLldpIfPol["children"] = []
        infraLLDP['infraRsLldpIfPol'] = infraRsLldpIfPol
        return infraLLDP, url

    def edit_lacpPolicy_InPCorvPC_policyGroup(self, policygrp_name, lacpPolicy_name):
        url = "/api/node/mo/uni/infra/funcprof/accbundle-{}/rslacpPol.json".format(policygrp_name)
        infraLACP = {}
        infraRsLacpIfPol = {}
        attributes = {}
        attributes["tnLacpLagPolName"] = lacpPolicy_name
        infraRsLacpIfPol["attributes"] = attributes
        infraRsLacpIfPol["children"] = []
        infraLACP['infraRsLacpPol'] = infraRsLacpIfPol
        return infraLACP, url

    def attach_vPCpolicy_to_EPG_payload(self, vlan, vPCPolicygrp):
        fvRsPathAtt_dic = {}
        fvRsPathAtt = {}
        attributes = {}
        attributes["encap"] = "vlan-{}".format(vlan)
        attributes["instrImedcy"] = "immediate"
        attributes["mode"] = "native"
        attributes["tDn"] = "topology/pod-1/protpaths-101-102/pathep-[{}]".format(vPCPolicygrp)
        attributes["status"] = "created"
        fvRsPathAtt["attributes"] = attributes
        fvRsPathAtt["children"] = []
        fvRsPathAtt_dic["fvRsPathAtt"] = fvRsPathAtt
        return fvRsPathAtt_dic

    def remove_vPCpolicy_from_EPG_payload(self, tenant_name, app_name, epg_name, policygrp_name):
        fvRsPathAtt_dic = {}
        fvRsPathAtt = {}
        attributes = {}
        attributes["dn"] = "uni/tn-{}/ap-{}/epg-{}/rspathAtt-[topology/pod-1/protpaths-101-102/pathep-[{}]]".format(tenant_name, app_name, epg_name, policygrp_name)
        attributes["status"] = "deleted"
        fvRsPathAtt["attributes"] = attributes
        fvRsPathAtt["children"] = []
        fvRsPathAtt_dic["fvRsPathAtt"] = fvRsPathAtt
        url = "/api/node/mo/uni/tn-{}/ap-{}/epg-{}/rspathAtt-[topology/pod-1/protpaths-101-102/pathep-[{}]].json".format(tenant_name, app_name, epg_name, policygrp_name)
        return fvRsPathAtt_dic, url

    def attach_PCpolicy_to_EPG_payload(self, vlan, PCPolicygrp, node):
        fvRsPathAtt_dic = {}
        fvRsPathAtt = {}
        attributes = {}
        attributes["encap"] = "vlan-{}".format(str(vlan))
        attributes["instrImedcy"] = "immediate"
        attributes["mode"] = "native"
        attributes["tDn"] = "topology/pod-1/paths-{}/pathep-[{}]".format(node, str(PCPolicygrp))
        attributes["status"] = "created"
        fvRsPathAtt["attributes"] = attributes
        fvRsPathAtt["children"] = []
        fvRsPathAtt_dic["fvRsPathAtt"] = fvRsPathAtt
        return fvRsPathAtt_dic

    def remove_PCpolicy_from_EPG_payload(self, tenant_name, app_name, epg_name, policygrp_name, node):
        fvRsPathAtt_dic = {}
        fvRsPathAtt = {}
        attributes = {}
        attributes["dn"] = "uni/tn-{}/ap-{}/epg-{}/rspathAtt-[topology/pod-1/paths-{}/pathep-[{}]]".format(tenant_name, app_name, epg_name, node, policygrp_name)
        attributes["status"] = "deleted"
        fvRsPathAtt["attributes"] = attributes
        fvRsPathAtt["children"] = []
        fvRsPathAtt_dic["fvRsPathAtt"] = fvRsPathAtt
        url = "/api/node/mo/uni/tn-{}/ap-{}/epg-{}/rspathAtt-[topology/pod-1/paths-{}/pathep-[{}]].json".format(tenant_name, app_name, epg_name, node, policygrp_name)
        return fvRsPathAtt_dic, url

    def CDP_policygrp_body_for_create(self, cdp_policy_grpName, adminState):
        infraPortGrp = {}
        cdp_attributes = {}
        attributes = {}
        attributes["dn"] = "uni/infra/cdpIfP-{}".format(cdp_policy_grpName)
        attributes["name"] = cdp_policy_grpName
        attributes["rn"] = "cdpIfP-{}".format(cdp_policy_grpName)
        attributes["status"] = "created"
        attributes["adminSt"] = adminState
        cdp_attributes["attributes"] = attributes
        cdp_attributes["children"] = []
        infraPortGrp["cdpIfPol"] = cdp_attributes
        return infraPortGrp

    def CDP_policygrp_body_for_edit(self, cdp_policy_grpName, adminState):
        infraPortGrp = {}
        cdp_attributes = {}
        attributes = {}
        attributes["dn"] = "uni/infra/cdpIfP-{}".format(cdp_policy_grpName)
        attributes["adminSt"] = adminState
        cdp_attributes["attributes"] = attributes
        cdp_attributes["children"] = []
        infraPortGrp["cdpIfPol"] = cdp_attributes
        return infraPortGrp

    def lldp_interfacepol_body_for_create(self, lldp_pol_name):
        infraPortGrp = {}
        lldp_attributes = {}
        attributes = {}
        attributes["dn"] = "uni/infra/lldpIfP-{}".format(lldp_pol_name)
        attributes["name"] = lldp_pol_name
        attributes["rn"] = "lldpIfP-{}".format(lldp_pol_name)
        attributes["status"] = "created"
        lldp_attributes["attributes"] = attributes
        lldp_attributes["children"] = []
        infraPortGrp["lldpIfPol"] = lldp_attributes
        return infraPortGrp

    def lldp_interfacepol_body_for_edit(self, lldp_pol_name, adminRxSt, adminTxSt):
        infraPortGrp = {}
        lldp_attributes = {}
        attributes = {}
        attributes["dn"] = "uni/infra/lldpIfP-{}".format(lldp_pol_name)
        attributes["adminRxSt"] = adminRxSt
        attributes["adminTxSt"] = adminTxSt
        lldp_attributes["attributes"] = attributes
        lldp_attributes["children"] = []
        infraPortGrp["lldpIfPol"] = lldp_attributes
        return infraPortGrp

    def aep_bodyBuild_for_create(self, aep_name, domain_name):
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
        attributes["dn"] = "uni/infra/attentp-{}".format(aep_name)
        attributes["name"] = aep_name
        attributes["rn"] = "attentp-{}".format(aep_name)
        attributes["status"] = "created"
        infraAttEntityP["attributes"] = attributes
        infraEntP['infraAttEntityP'] = infraAttEntityP
        infraEntP['infraAttEntityP'].update(self.chldrn_data(domain_name))
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

    def chldrn_data(self, domain_name):
        chldrn = {}
        chldrn["children"] = []
        infraEntP = {}
        infraRsDomP = {}
        attributes = {}
        attributes["tDn"] = "uni/phys-{}".format(domain_name)
        attributes["status"] = "created"
        infraRsDomP["attributes"] = attributes
        infraRsDomP["children"] = []
        infraEntP["infraRsDomP"] = infraRsDomP
        chldrn["children"].append(infraEntP)
        return chldrn

    def aep_bodyBuild_for_edit(self, physicalDomain_name):
        infraRsDomP = {}
        infraRsDomP_attributes = {}
        attributes = {}
        attributes["tDn"] = "uni/phys-{}".format(physicalDomain_name)
        attributes["status"] = "created"
        infraRsDomP_attributes["attributes"] = attributes
        infraRsDomP_attributes["children"] = []
        infraRsDomP["infraRsDomP"] = infraRsDomP_attributes
        return infraRsDomP

    def physicalDomain_bodyBuild_forCreate(self, pd_name, vlan_pool_name):
        physDomP = {}
        physDomPAttributes = {}
        attributes = {}
        attributes["dn"] = "uni/phys-{}".format(pd_name)
        attributes["name"] = pd_name
        attributes["rn"] = "phys-{}".format(pd_name)
        attributes["status"] = "created"
        physDomPAttributes["attributes"] = attributes
        physDomP["physDomP"] = physDomPAttributes

        chldrn = {}
        chldrn["children"] = []
        infraRsVlanNs = {}
        infraRsVlanNs_attributes = {}
        attributes = {}
        attributes["tDn"] = "uni/infra/vlanns-[{}]-static".format(vlan_pool_name)
        attributes["status"] = "created"
        infraRsVlanNs_attributes["attributes"] = attributes
        infraRsVlanNs_attributes["children"] = []
        infraRsVlanNs["infraRsVlanNs"] = infraRsVlanNs_attributes
        chldrn["children"].append(infraRsVlanNs)

        physDomP["physDomP"] = physDomPAttributes
        physDomP["physDomP"].update(chldrn)
        return physDomP

    def attach_aep_to_physicalDomain_bodyBuild(self, pd_name):
        infraRsDomP = {}
        infraRsDomP_attributes = {}
        attributes = {}
        attributes["tDn"] = "uni/phys-{}".format(pd_name)
        attributes["status"] = "created,modified"
        infraRsDomP_attributes["attributes"] = attributes
        infraRsDomP_attributes["children"] = []
        infraRsDomP["infraRsDomP"] = infraRsDomP_attributes
        return infraRsDomP

    def edit_physical_domain(self, vlan_poolName):
        infraRsVlanNs = {}
        infraRsVlanNs_attributes = {}
        attributes = {}
        attributes["tDn"] = "uni/infra/vlanns-[{}]-static".format(vlan_poolName)
        infraRsVlanNs_attributes["attributes"] = attributes
        infraRsVlanNs_attributes["children"] = []
        infraRsVlanNs["infraRsVlanNs"] = infraRsVlanNs_attributes
        return infraRsVlanNs

    def interface_profile_payload_forCreate(self, switch_prfl, profile_name, from_port, to_port, policygrp_name):
        infraHPortS = {}
        infraHPortS_attributes = {}
        attributes = {}
        attributes["dn"] = "uni/infra/accportprof-{}/hports-{}-typ-range".format(switch_prfl, profile_name)
        attributes["name"] = profile_name
        attributes["rn"] = "hports-{}-typ-range".format(profile_name)
        attributes["status"] = "created,modified"
        infraHPortS_attributes["attributes"] = attributes
        infraHPortS["infraHPortS"] = infraHPortS_attributes

        children = {}
        children["children"] = []

        infraPortBlk = {}
        infraPortBlkAttributes = {}
        attributes = {}
        attributes["dn"] = "uni/infra/accportprof-{}/hports-{}-typ-range/portblk-block2".format(switch_prfl, profile_name)
        attributes["fromPort"] = "{}".format(from_port)
        attributes["toPort"] = "{}".format(to_port)
        attributes["name"] = "block2"
        attributes["rn"] = "portblk-block2"
        attributes["status"] = "created,modified"
        infraPortBlkAttributes["attributes"] = attributes
        infraPortBlkAttributes["children"] = []
        infraPortBlk["infraPortBlk"] = infraPortBlkAttributes

        infraRsAccBaseGrp = {}
        infraRsAccBaseGrpAttributes = {}
        attributes = {}
        attributes["tDn"] = "uni/infra/funcprof/accportgrp-{}".format(policygrp_name)
        attributes["status"] = "created,modified"
        infraRsAccBaseGrpAttributes["attributes"] = attributes
        infraRsAccBaseGrpAttributes["children"] = []
        infraRsAccBaseGrp["infraRsAccBaseGrp"] = infraRsAccBaseGrpAttributes

        children["children"].append(infraPortBlk)
        children["children"].append(infraRsAccBaseGrp)

        infraHPortS["infraHPortS"].update(children)
        return infraHPortS

    def get_controllers(self, session, domain):  # This method used to get the list of controllers in the domain
        url = "/api/node/class/compCtrlr.json?query-target-filter=and(eq(compCtrlr.domName,%22{}%22),wcard(compCtrlr.ctrlrPKey,%22^uni/vmmp-VMware/dom-.%22))".format(domain)
        response = session.get(url).json()
        imdata = response['imdata']
        objcount = response['totalCount']
        domainsList = []
        if int(objcount) > 0:
            for domainslist in imdata:
                domains = domainslist['compCtrlr']
                attrib = domains['attributes']
                domainsList.append(attrib['name'])
        return domainsList

    def get_portGroups(self, session, domain, controller, portgrp_map_string):  # This method used to get the list of port groups in the domain controller
        url = "/api/node/mo/comp/prov-VMware/ctrlr-[{}]-{}.json?query-target=children&target-subtree-class=hvsLNode".format(domain, controller[0])
        response1 = session.get(url).json()
        imdata1 = response1['imdata']
        dvs_switch_id = ''
        for data in imdata1:
            dvs_switch_id = data['hvsLNode']['attributes']['oid']
        url1 = "/api/node/mo/comp/prov-VMware/ctrlr-[{}]-{}/sw-{}.json?query-target=children&target-subtree-class=hvsExtPol".format(domain, controller[0], dvs_switch_id)
        response = session.get(url1).json()
        objcount = response['totalCount']
        imdata = response['imdata']
        portGroupList = []
        if int(objcount) > 0:
            for domainslist in imdata:
                domains = domainslist['hvsExtPol']
                attrib = domains['attributes']
                if attrib['name'] == portgrp_map_string:
                    if attrib['startEncap'] == attrib['endEncap']:
                        portGroupList.append(str(attrib['endEncap']).replace("vlan-", ''))
                    else:
                        endVlan = str(attrib['endEncap']).replace("vlan-", '')
                        startVlan = str(attrib['startEncap']).replace("vlan-", '')
                        portGroupList.append(startVlan + "-" + endVlan)
        return portGroupList

    def get_portGroups_listOfAll(self, session, domain, controller):  # This method used to get the list of port groups in the domain controller
        url = "/api/node/mo/comp/prov-VMware/ctrlr-[{}]-{}.json?query-target=children&target-subtree-class=hvsLNode".format(domain, controller[0])
        response1 = session.get(url).json()
        imdata1 = response1['imdata']
        dvs_switch_id = ''
        for data in imdata1:
            dvs_switch_id = data['hvsLNode']['attributes']['oid']
        url1 = "/api/node/mo/comp/prov-VMware/ctrlr-[{}]-{}/sw-{}.json?query-target=children&target-subtree-class=hvsExtPol".format(domain, controller[0], dvs_switch_id)
        response = session.get(url1).json()
        objcount = response['totalCount']
        imdata = response['imdata']
        portGroupList = []
        if int(objcount) > 0:
            for domainslist in imdata:
                domains = domainslist['hvsExtPol']
                attrib = domains['attributes']
                if attrib['startEncap'] == attrib['endEncap']:
                    portGroupList.append(str(attrib['endEncap']).replace("vlan-", ''))
                else:
                    endVlan = str(attrib['endEncap']).replace("vlan-", '')
                    startVlan = str(attrib['startEncap']).replace("vlan-", '')
                    portGroupList.append(startVlan + "-" + endVlan)
        return portGroupList

    def get_portGroups_vlansList_givenTenant(self, session, domain, controller, tenant_name):  # This method used to get the list of port groups in the domain controller
        url = "/api/node/mo/comp/prov-VMware/ctrlr-[{}]-{}.json?query-target=children&target-subtree-class=hvsLNode".format(domain, controller[0])
        response1 = session.get(url).json()
        imdata1 = response1['imdata']
        dvs_switch_id = ''
        for data in imdata1:
            dvs_switch_id = data['hvsLNode']['attributes']['oid']
        url1 = "/api/node/mo/comp/prov-VMware/ctrlr-[{}]-{}/sw-{}.json?query-target=children&target-subtree-class=hvsExtPol".format(domain, controller[0], dvs_switch_id)
        response = session.get(url1).json()
        objcount = response['totalCount']
        imdata = response['imdata']
        portGroupList = []
        if int(objcount) > 0:
            for domainslist in imdata:
                domains = domainslist['hvsExtPol']
                attrib = domains['attributes']
                if tenant_name in attrib['name']:
                    if attrib['startEncap'] == attrib['endEncap']:
                        portGroupList.append(str(attrib['endEncap']).replace("vlan-", ''))
                    else:
                        endVlan = str(attrib['endEncap']).replace("vlan-", '')
                        startVlan = str(attrib['startEncap']).replace("vlan-", '')
                        portGroupList.append(startVlan + "-" + endVlan)
        return portGroupList

    def get_tenant_staticBinding_dynamic_vlans(self, session, tenant_name, vmmDomain_name):
        static_vlan_list = self.get_Tenant_VLANList(session, tenant_name)
        # print len(static_vlan_list)
        controller = self.get_controllers(session, vmmDomain_name)
        dynamic_vlans = self.get_portGroups_vlansList_givenTenant(session, vmmDomain_name, controller, tenant_name)
        # print len(dynamic_vlans)
        sb_dynamic_vlans = static_vlan_list + dynamic_vlans
        # print len(sb_dynamic_vlans)
        return sb_dynamic_vlans


class APICResources:

    def getf_access_entity_profiles(self, session):
        url = "/api/node/mo/uni/infra.json?query-target=subtree&target-subtree-class=infraAttEntityP"
        response = session.get(url).json()
        imdata = response['imdata']
        return imdata

    def get_domains(self, session, aep_name):
        url = "/api/node/mo/uni/infra/attentp-{}.json?query-target=children&target-subtree-class=infraRsDomP".format(aep_name)
        response = session.get(url).json()
        return response['imdata']

    def getf_cdp_interface_policies(self, session):
        url = "/api/node/class/cdpIfPol.json?query-target=subtree&target-subtree-class=cdpIfPol"
        response = session.get(url).json()
        imdata = response['imdata']
        return imdata

    def getf_cdp_interface_policies(self, session):
        url = "/api/node/class/cdpIfPol.json?query-target=subtree&target-subtree-class=cdpIfPol"
        response = session.get(url).json()
        imdata = response['imdata']
        return imdata

    def getf_lldp_interface_policies(self, session):
        url = "/api/node/mo/uni/infra.json?query-target=children&target-subtree-class=lldpIfPol"
        response = session.get(url).json()
        imdata = response['imdata']
        return imdata

    def get_physical_domain(self, session):
        url = "/api/node/mo/uni.json?query-target=subtree&target-subtree-class=physDomP&target-subtree-class=infraRsVlanNs"
        response = session.get(url).json()
        imdata = response['imdata']
        return imdata

    def getf_portchannel_policies(self, session):
        url = "/api/node/mo/uni/infra.json?query-target=children&target-subtree-class=lacpLagPol"
        response = session.get(url).json()
        imdata = response['imdata']
        return imdata

    def getf_switch_leaf_profiles(self, session):
        url = "/api/node/mo/uni/infra.json?query-target=subtree&target-subtree-class=infraNodeBlk"
        response = session.get(url).json()
        imdata = response['imdata']
        logger._log(imdata)
        return imdata

    def getf_vlan_pools(self, session):
        url = "/api/node/class/fvnsVlanInstP.json?query-target=subtree&target-subtree-class=fvnsEncapBlk"
        response = session.get(url).json()
        imdata = response['imdata']
        logger._log(imdata)
        return imdata

    def get_vmm_domain(self, session):
        url = "/api/node/mo/comp/prov-VMware.json?query-target=children&target-subtree-class=compDom"
        response = session.get(url).json()
        imdata = response['imdata']
        return imdata


class AttachInterface:

    def get_apic_session(self, url, username, password):
        apic_session = aci.Session(url, username, password)
        res = apic_session.login()
        if not res.ok:
            error = ["Could not login to APIC."]
            error += re.findall("text\":\"(.*)\"", res.content)
            raise Exception(" ".join(error))
        return apic_session

    def add_static_binding_interface(self, session, user_tenant, user_appProfile, epg_name):
        INTERFACE = {'type': 'eth', 'pod': '1', 'node': '101', 'module': '1', 'port': '21'}
        VLAN = {'name': 'vlan5', 'encap_type': 'vlan', 'encap_id': '1005'}
        # Create the physical interface object
        intf = ACI.Interface(INTERFACE['type'],
                             INTERFACE['pod'],
                             INTERFACE['node'],
                             INTERFACE['module'],
                             INTERFACE['port'])

        tenants = aci.Tenant.get(session)
        tflg = False
        appflg = False
        epgflg = False
        tenant_available = object
        epg_available = object
        for tenant in tenants:
            if str(tenant) == user_tenant:
                tenant_available = tenant
                tflg = True
                apps = aci.AppProfile.get(session, tenant)
                for app in apps:
                    if str(app) == user_appProfile:
                        appflg = True
                        epgs = aci.EPG.get(session, app, tenant)
                        for epg in epgs:
                            if str(epg) == epg_name:
                                epgflg = True
                                epg_available = epg

        if tflg:
            if appflg:
                if epgflg:
                    vlan_intf = ACI.L2Interface(VLAN['name'], VLAN['encap_type'], VLAN['encap_id'])
                    vlan_intf.attach(intf)
                    epg_available.attach(vlan_intf)
                    resp = tenant_available.push_to_apic(session)
                    if not resp.ok:
                        print('%% Error: Could not push tenant configuration to APIC')
                        print resp, "Tenant"

                    # Push the interface attachment to the APIC
                    resp = intf.push_to_apic(session)
                    if not resp.ok:
                        print('%% Error: Could not push interface configuration to APIC')
                        print resp, "int conf"

                    print "Jithendra"
                else:
                    logger._log("*** {} EPG is not available in APIC".format(epg_name))
            else:
                logger._log("*** {} App Profile is not Available in APIC".format(user_appProfile))
        else:
            logger._log("*** {} Tenant is not available in APIC".format(user_tenant))


obj = AttachInterface()
sess = obj.get_apic_session("https://192.168.144.114", "admin", "password")
domain = 'Automation_Wipro_VMM'
tenant_name = 'Test_tenant2'
app_profile = 'Test_App2'
epg_name = 'Test_epg3'
obj.add_static_binding_interface(sess, tenant_name, app_profile, epg_name)
