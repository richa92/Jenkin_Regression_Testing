"""
instant_clone.py

This script will use VMware's instant cloning feature to make a up and running clone of a vm.
The number of clones produced is derived from the amount of IPs in the range provided.

Prerequisites:
ESXi 6.7 (instant cloning feature is available as of this release)
vCenter or VCSA 6.7
Customization script that can handle the specific parent OS
Source\parent VM configured as desired (i.e. firewalls, tools, services), including customization script
Access to RoboGalaxy from a TCS to run this script

Process:
1. start the customization script on the parent vm
2. run this script, specifying the vCenter creds, desired IP range, and parent vm name in the vars below
"""
from RoboGalaxyLibrary import VsphereKeywords


def ip_range(start_ip, end_ip):
    start = list(map(int, start_ip.split(".")))
    end = list(map(int, end_ip.split(".")))
    temp = start
    ip_range = list()

    ip_range.append(start_ip)
    while temp != end:
        start[3] += 1
        for i in (3, 2, 1):
            if temp[i] == 255:
                temp[i] = 1
                temp[i - 1] += 1
        ip_range.append(".".join(map(str, temp)))

    return ip_range


v = VsphereKeywords()
s = v.connect_to_vi_server('10.177.14.101', 'administrator@vsphere.local', 'Plexxi@123')
parentvm = 'centos7.6'

ips = ip_range("10.177.15.1", "10.177.15.254")

# TODO: if multiple parent vms (one on each host to split load up), iterate hosts

for count, ip in enumerate(ips, start=1):

    icspec = {'name': '{}_{}'.format(parentvm, str(count)),
              'location': {},
              'config': {'guestinfo.ic.hostname': '{}_{}'.format(parentvm, str(count)),
                         'guestinfo.ic.ipv4': ip,
                         'guestinfo.ic.netmask': '255.255.0.0',   # 21
                         'guestinfo.ic.dns': '10.171.0.11',
                         'guestinfo.ic.gateway': '10.177.0.1'}}

    result = v.create_instant_clone(parentvm, icspec)
