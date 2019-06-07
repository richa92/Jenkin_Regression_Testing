#!/usr/bin/env python27
# (C) Copyright 2018 Hewlett Packard Enterprise Development LP
"""
Data variables file for os_deploy_test_case.robot

The Keyword documentation is available at <FusionLibrary/keywords/cpt>
"""


# A sample OS profile dictionary

def make_cpt_batch(sh_cpt, pfs):
    """
    return a bunch of cpt profiles based on a given list of profile names
    :param sh_cpt: the server_hardware_cpt list variable value from the datafile
    :param pfs: You can provide a list() of profile names from this python module, or comma separated on command line
    ex: -v cpt_profiles: ProfileR1_U1,ProfileR1_U2
    :return: a subset of server_hardware_cpt data
    """
    if pfs is None:
        return sh_cpt
    if isinstance(pfs, list):
        return [s for s in sh_cpt if s['profile'] in pfs]
    return [s for s in sh_cpt if s['profile'] in pfs.split(',')]


def create_seed(os, net, ilou, ilop):
    return {"os_name": os['os_name'],
            "os_repo": os['os_repo'],
            "deployment_network": net,
            "ilo_user": ilou,
            "ilo_pass": ilop,
            "system_password": "Hpvse123!"
            }


WIN2016 = {"os_name": "Win2016_DTC_x64",
           "os_repo": r"\\192.168.1.1\win2016",
           }

WIN2019 = {"os_name": "Win2019_DTC_x64",
           "os_repo": r"\\192.168.1.1\win2019",
           }

ESXi65 = {"os_name": "ESXi65x64",
          "os_repo": "http://192.168.1.1/deployment/iso/vmware/VMware-ESXi-6.5.0-Update2-9298722-HPE-Gen9plus-650.U2.10.4.0.4-Mar2019.iso",
          }

ESXi67 = {"os_name": "ESXi67x64",
          "os_repo": "http://192.168.1.1/deployment/iso/vmware/VMware-ESXi-6.7.0-OS-Release-9256182-HPE-Gen9plus-670.U1.10.3.0.7-Oct2018.iso",
          }

# Details of the system hosting Cirrus Provisioning Tool
cpt_host = {"host": "192.168.1.1",
            "user": "root",
            "password": "rootpwd"}

server_hardware = [
    # rack u #1
    {
        "hostname": "10.172.12.12",
        "username": "Administrator",
        "password": "RYDNCSRD",
        "force": True,
        "licensingIntent": "OneView",
        "configurationState": "Managed",
        "deployment_network": "VlanTrunk1-O",
        "os": WIN2016,
        "profile": "ProfileU1"

    },
    # rack u #2
    {
        "hostname": "10.172.12.9",
        "username": "Administrator",
        "password": "U59PJ685",
        "force": True,
        "licensingIntent": "OneView",
        "configurationState": "Managed",
        "deployment_network": "VlanTrunk1-O",
        "os": ESXi67,
        "profile": "ProfileU2"

    },
    # rack u #3
    {
        "hostname": "10.172.12.7",
        "username": "Administrator",
        "password": "7J4AAE93",
        "force": True,
        "licensingIntent": "OneView",
        "configurationState": "Managed",
        "deployment_network": "VlanTrunk1-O",
        "os": ESXi67,
        "profile": "ProfileU3"

    },
    # rack u #4
    {
        "hostname": "10.172.12.24",
        "username": "Administrator",
        "password": "7BMUAQPM",
        "force": True,
        "licensingIntent": "OneView",
        "configurationState": "Managed",
        "deployment_network": "VlanTrunk1-O",
        "os": ESXi67,
        "profile": "ProfileU4"
    },
]

server_hardware = [{
    "hostname": "10.172.12.12",
    "username": "Administrator",
    "password": "RYDNCSRD",
    "force": True,
    "licensingIntent": "OneView",
    "configurationState": "Managed",
    "deployment_network": "VlanTrunk1-O",
    "os": WIN2019,
    "profile": "ProfileU1"

}]
