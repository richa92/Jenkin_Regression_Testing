from acitoolkit.acitoolkit import Tenant, Context, BridgeDomain, AppProfile
from acitoolkit.acitoolkit import EPG, Interface, L2Interface, Session
from acitoolkit.acitoolkit import Credentials
import acitoolkit.acitoolkit as aci
import time


def send_to_apic():
    """
    Login to APIC and push the config
    :param tenant: Tenant class instance
    :return: request response object
    """
    description = 'Basic Connectivity Example'
    creds = Credentials('apic', description)
    args = creds.get()
    # Login to APIC
    session = Session(args.url, args.login, args.password, False)
    session.login()
    tenants = aci.Tenant.get(session)
    user_tenant = "OneView-APIC-Tenant-1"
    user_appProfile = "OneView-APIC-AppProfile-1"
    for tenant in tenants:
        if str(tenant) == user_tenant.strip():
            apps = aci.AppProfile.get(session, tenant)
            for app in apps:
                if str(app) == user_appProfile:
                    epg1 = "EPG"
                    for number in range(0, 10):
                        epgg = epg1 + str(number)
                        epg = EPG(epgg, app)
                        domains = aci.VmmDomain.get(session)
                        for domain in domains:
                            if str(domain) == "OneView-APIC-vSwitch-Bay1":
                                epg.attach(domain)
        resp = tenant.push_to_apic(session)

# Create the 165 EPG's


def main():
    send_to_apic()
if __name__ == '__main__':
    main()
