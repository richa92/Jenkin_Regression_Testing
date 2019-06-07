#!/usr/bin/env python27
# (C) Copyright 2018 Hewlett Packard Enterprise Development LP
"""
Data variables file for os_deploy_test_case.robot

The Keyword documentation is available at <FusionLibrary/keywords/cpt>
"""
# A sample OS profile dictionary
ESXi65 = {"os_name": "ESXi65x64",
          "os_repo": "http://192.168.124.10/iso/esxi/65.iso",
          "deployment_network": "icsp",
          "ilo_user": "Administrator",
          "ilo_pass": "admin123"}

# Details of the system hosting Cirrus Provisioning Tool
cpt_host = {"host": "192.168.124.20",
            "user": "root",
            "password": "hpvse123"}
