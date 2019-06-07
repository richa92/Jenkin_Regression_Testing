from acitoolkit.acitoolkit import EPG, Interface, L2Interface, Session
from acitoolkit.acitoolkit import Credentials
import acitoolkit.acitoolkit as aci
import re
"""
This script used to delete the EPGs with matching with "EPG" string.
"""


def EPG_deletion():
    description = 'Basic Connectivity Example'
    creds = Credentials('apic', description)
    args = creds.get()
    # Login to APIC
    session = Session(args.url, args.login, args.password, False)
    session.login()
    tenants = aci.Tenant.get(session)
    for tenant in tenants:
        apps = aci.AppProfile.get(session, tenant)
        for app in apps:
            epgs = aci.EPG.get(session, app, tenant)
            for epg in epgs:
                if re.match("EPG\d+", str(epg)):
                    epg.mark_as_deleted()
                    resp = tenant.push_to_apic(session)
                    if resp.ok:
                        print "Deleted", str(epg)
                    else:
                        print 'Could not delete tenant', str(epg)
                        print resp.text
if __name__ == '__main__':
    EPG_deletion()
