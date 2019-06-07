#!/usr/bin/env python27
# (C) Copyright 2018 Hewlett Packard Enterprise Development LP
"""
Sample network and host profile variables that are inputs to the generator
"""
OV = {'host': '192.168.0.11',
      'cred': {'userName': 'Administrator', 'password': 'somepassword'}}

HOST = {
    "rhel": {
        "ipv4": "192.168.10.20",
        "user": "root",
        "password": "somepassword",
        "os": "RedHat Enterprise Linux 6"
    },
    "esx": {
        "ipv4": "192.168.10.21",
        "user": "root",
        "password": "somepassword",
        "os": "rhel"},
    "esxi": {
        "ipv4": "192.168.10.22",
        "user": "root",
        "passowrd": "somepassword",
        "os": "VMware ESXi 6.1",
        "datacenter": "FTC_DC",
        "cluster": "TestCluster",
        "manager": {
            "ipv4": "192.168.0.10",
            "user": "administrator@vsphere.local",
            "password": "somepassword"
        }
    }}

cfg_rhel_eth = {"ov_network": "deploy_net",
                "type": "ethernet",
                "name": "bootnet"}

cfg_rhel_bond = {"ov_network": "dataNetSet",
                 "type": "bond",
                 "name": "dataNet",
                 "bond_opts": "mode=active-backup,miimon=100"}

cfg_rhel_team = {"ov_network": "highNetSet",
                 "type": "team",
                 "team_opts": '{"runner": {"name": "activebackup"}}',
                 "team_port_cfg": ['{"prio": 100}', '{"prio": 10}}']}

cfg_esx_vss = {"ov_network": "deploy_net",
               "type": "vss",
               "name": "deploySwitch",
               "network": {100: {'vmk': True}}}

cfg_esx_vs2 = {"ov_network": "highNetSet",
               "type": "vss",
               "name": "highNetSwitch",
               "network": {200: {'vmk': True},
                           201: {'vmk': False,
                                 'policy': 'loadbalance_ip'},
                           202: {'policy': 'loadbalance_loadbased'}}}

cfg_esx_vds = {"ov_network": "dataNetSet",
               "type": "vds",
               "name": "dataSwitch",
               "network": {300: {'vmk': True},
                           301: {'vmk': False,
                                 'policy': 'loadbalance_ip'},
                           302: {'policy': 'loadbalance_loadbased'}}}

RHEL_NP_1 = [cfg_rhel_eth, cfg_rhel_bond]
RHEL_NP_2 = [cfg_rhel_eth, cfg_rhel_bond, cfg_rhel_team]
ESXI_NP_1 = [cfg_esx_vss, cfg_esx_vs2]
ESXI_NF_2 = [cfg_esx_vds]
