import re
import time
from acitoolkit.acitoolkit import Interface, PortChannel, Tenant, AppProfile, L2Interface, EPG
import acitoolkit.acitoolkit as aci
from acitoolkit.acitoolkit import Credentials, Session


class TenantScalabilty:

    def get_apic_session(self):
        description = 'Basic Connectivity Example'
        creds = Credentials('apic', description)
        args = creds.get()
        apic_session = Session(args.url, args.login, args.password, False)
        apic_session.login()
        return apic_session

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
                    print("*** {} Tenant Created".format(str(tenant)))
            else:
                print('%% Error: Could not push configuration to APIC')

    def delete_tenant_for_scalabilityTest(self, session):
        tenants = Tenant.get(session)
        for tenant in tenants:
            if re.match("FVT_TenantScale_Test\d+", str(tenant)):
                tenant.mark_as_deleted()
                resp = session.push_to_apic(tenant.get_url(), tenant.get_json())
                if resp.ok:
                    print('***{} Tenant Deleted'.format(str(tenant)))

number_tenants_tobe_created = 50
domain_toBe_attached = "OneView-APIC-vSwitch-Bay2"
objforTenatnscale = TenantScalabilty()
session = objforTenatnscale.get_apic_session()
objforTenatnscale.create_tenant_for_scalabilityTest(session, number_tenants_tobe_created, domain_toBe_attached)
