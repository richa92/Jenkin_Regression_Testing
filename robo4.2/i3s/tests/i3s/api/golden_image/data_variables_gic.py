#!/usr/bin/python
# -*- coding: utf-8 -*-

"""Credentials to login to Fusion."""


ADMIN_CREDENTIALS = {'userName': 'Administrator',
                     'password': 'admin123'}


"""Golden Image Capture test data."""
CREATEGOLDENIMAGE = [
    {
        'type': 'GoldenImage',
        'name': 'Test',
        'description': 'Test',
        'imageCapture': 'true',
        'osVolumeURI': 'sp_osvolume_for_gic',
        'buildPlanUri': 'bp_for_gic',
        },
    {
        'type': 'GoldenImage',
        'name': 'Test',
        'description': 'Duplicate Name',
        'imageCapture': 'true',
        'osVolumeURI': 'sp_osvolume_for_gic',
        'buildPlanUri': 'bp_for_gic',
        },
    {
        'type': 'GoldenImage',
        'name': '',
        'description': 'Name field null',
        'imageCapture': 'true',
        'osVolumeURI': 'sp_osvolume_for_gic',
        'buildPlanUri': 'bp_for_gic',
        },
    {
        'type': '',
        'name': '',
        'description': '',
        'imageCapture': '',
        'osVolumeURI': '',
        'buildPlanUri': '',
        },
    {
        'type': 'GoldenImage',
        'name': '%#$*%',
        'description': 'Gi with invalid name',
        'imageCapture': 'true',
        'osVolumeURI': 'sp_osvolume_for_gic',
        'buildPlanUri': 'bp_for_gic',
        },
    {
        'type': 'GoldenImage',
        'name': 'goldenimagecapturegoldenimagecapturegoldenimagecapturegoldenimagecapturegoldenimagecapturegoldenimagecapturegoldenimagecapturegoldenimagecapturegoldenimagecapturegoldenimagecapturegoldenimagecapturegoldenimagecapturegoldenimagecapturegoldenimagecapturegol',
        'description': 'Gi name with max char',
        'imageCapture': 'true',
        'osVolumeURI': 'sp_osvolume_for_gic',
        'buildPlanUri': 'bp_for_gic',
        },
    {
        'type': 'GoldenImage',
        'name': 'goldenimagecapturegoldenimagecapturegoldenimagecapturegoldenimagecapturegoldenimagecapturegoldenimagecapturegoldenimagecapturegoldenimagecapturegoldenimagecapturegoldenimagecapturegoldenimagecapturegoldenimagecapturegoldenimagecapturegoldenimagecapturegold',
        'description': 'Gi with name greater than 255 chars',
        'imageCapture': 'true',
        'osVolumeURI': 'sp_osvolume_for_gic',
        'buildPlanUri': 'bp_for_gic',
        },
    {
        'type': 'GoldenImage',
        'name': 'descmaxchar 1000',
        'description': 'goldenimagecapturedescgoldenimagecapturedescgoldenimagecapturedescgoldenimagecapturedescgoldenimagecapturedescgoldenimagecapturedescgoldenimagecapturedescgoldenimagecapturedescgoldenimagecapturedescgoldenimagecapturedescgoldenimagecapturedescgoldenimagecapturedescgoldenimagecapturedescgoldenimagecapturedescgoldenimagecapturedescgoldenimagecapturedescgoldenimagecapturedescgoldenimagecapturedescgoldenimagecapturedescgoldenimagecapturedescgoldenimagecapturedescgoldenimagecapturedescgoldenimagecapturedescgoldenimagecapturedescgoldenimagecapturedescgoldenimagecapturedescgoldenimagecapturedescgoldenimagecapturedescgoldenimagecapturedescgoldenimagecapturedescgoldenimagecapturedescgoldenimagecapturedescgoldenimagecapturedescgoldenimagecapturedescgoldenimagecapturedescgoldenimagecapturedescgoldenimagecapturedescgoldenimagecapturedescgoldenimagecapturedescgoldenimagecapturedescgoldenimagecapturedescgoldenimagecapturedescgoldenimagecapturedescgoldenimagecapturedescgoldenimagecapturedescgoldenimag',
        'imageCapture': 'true',
        'osVolumeURI': 'sp_osvolume_for_gic',
        'buildPlanUri': 'bp_for_gic',
        },
    {
        'type': 'GoldenImage',
        'name': 'desc greater than  1000 char',
        'description': 'goldenimagecapturedescgoldenimagecapturedescgoldenimagecapturedescgoldenimagecapturedescgoldenimagecapturedescgoldenimagecapturedescgoldenimagecapturedescgoldenimagecapturedescgoldenimagecapturedescgoldenimagecapturedescgoldenimagecapturedescgoldenimagecapturedescgoldenimagecapturedescgoldenimagecapturedescgoldenimagecapturedescgoldenimagecapturedescgoldenimagecapturedescgoldenimagecapturedescgoldenimagecapturedescgoldenimagecapturedescgoldenimagecapturedescgoldenimagecapturedescgoldenimagecapturedescgoldenimagecapturedescgoldenimagecapturedescgoldenimagecapturedescgoldenimagecapturedescgoldenimagecapturedescgoldenimagecapturedescgoldenimagecapturedescgoldenimagecapturedescgoldenimagecapturedescgoldenimagecapturedescgoldenimagecapturedescgoldenimagecapturedescgoldenimagecapturedescgoldenimagecapturedescgoldenimagecapturedescgoldenimagecapturedescgoldenimagecapturedescgoldenimagecapturedescgoldenimagecapturedescgoldenimagecapturedescgoldenimagecapturedescgoldenimagecapturedescgoldenimaged',
        'imageCapture': 'true',
        'osVolumeURI': 'sp_osvolume_for_gic',
        'buildPlanUri': 'bp_for_gic',
        },
    {
        'type': 'GoldenImage',
        'name': 'Gi_no_buildstep',
        'description': 'buildplan with no buildstep',
        'imageCapture': 'true',
        'osVolumeURI': 'sp_osvolume_for_gic',
        'buildPlanUri': 'bp_for_gic_with_no_buildstep',
        },
    {
        'type': 'GoldenImage',
        'name': 'Gi_no_server profile',
        'description': 'Non existing server profile',
        'imageCapture': 'true',
        'osVolumeURI': 'do_not_exist_sp_osvolume_for_gic',
        'buildPlanUri': 'bp_for_gic',
        },
    {
        'type': 'GoldenImage',
        'name': 'Gi_no_bp',
        'description': 'Test',
        'imageCapture': 'true',
        'osVolumeURI': 'sp_osvolume_for_gic',
        'buildPlanUri': 'do_no_exist_bp_for_gic',
        },
    {
        'type': 'GoldenImage',
        'name': 'Gi_no_bp_no_sp',
        'description': 'Test',
        'imageCapture': 'true',
        'osVolumeURI': 'do_not_exist_sp_osvolume_for_gic',
        'buildPlanUri': 'do_no_exist_bp_for_gic',
        },
    {
        'type': 'GoldenImage',
        'name': 'Gi_bp_type_deploy',
        'description': 'Test',
        'imageCapture': 'true',
        'osVolumeURI': 'sp_osvolume_for_gic',
        'buildPlanUri': 'bp_type_deploy',
        },
    {
        'type': 'GoldenImage',
        'name': 'Gi_blank_sp_bp',
        'description': 'Test',
        'imageCapture': 'true',
        'osVolumeURI': '',
        'buildPlanUri': '',
        },
    ]

"""Server profile json body."""

SERVERPROFILE_GIC = {
    'type': 'ServerProfileV11',
    'name': 'sp_osvolume_for_gic',
    'iscsiInitiatorNameType': 'AutoGenerated',
    'serverHardwareUri': ' CN75450628, bay 5',
    'serverHardwareTypeUri': 'SY 660 Gen9 1',
    'enclosureGroupUri': 'EG',
    'enclosureUri': 'CN75450628',
    'affinity': 'Bay',
    'hideUnusedFlexNics': True,
    'firmware': {
        'firmwareInstallType': None,
        'forceInstallFirmware': False,
        'manageFirmware': False,
        'firmwareBaselineUri': None,
        },
    'macType': 'Virtual',
    'wwnType': 'Virtual',
    'osDeploymentSettings': {
        'osDeploymentPlanUri': 'dp_esxi6_20_full',
        'osCustomAttributes': [{
            'name': 'hostname',
            'value': 'hostbay7'
            }],
        'osVolumeUri': None
        },
    'connections': [{
        'id': 1,
        'name': 'Deployment Network A',
        'functionType': 'Ethernet',
        'networkUri': ['Deploy'],
        'portId': 'Mezz 3:1-a',
        'requestedVFs': 'Auto',
        'allocatedVFs': 24,
        'macType': 'Virtual',
        'wwpnType': 'Virtual',
        'mac': '',
        'requestedMbps': '2500',
        'allocatedMbps': 2500,
        'maximumMbps': 20000,
        'boot': {'priority': 'Primary', 'ethernetBootType': 'iSCSI',
                 'iscsi': {
                     'initiatorNameSource': 'ProfileInitiatorName',
                     'firstBootTargetIp': None,
                     'secondBootTargetIp': '',
                     'secondBootTargetPort': '',
                     'initiatorName': None,
                     'bootTargetName': None,
                     'bootTargetLun': None
                     }
                 },
        }],
    'bootMode': {'manageMode': True, 'pxeBootPolicy': 'Auto',
                 'mode': 'UEFIOptimized'},
    'boot': {'manageBoot': True, 'order': []},
    'bios': {'manageBios': False, 'overriddenSettings': []},
    'localStorage': {},
    'sanStorage': {'volumeAttachments': [], 'manageSanStorage': False},
    }
