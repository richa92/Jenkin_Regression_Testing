#!/usr/bin/python
"""
Description: The script read the /proc/net/bonding/bond* files, convert the data into dictionary with options available to simply pretty print it or use the data to test via available arguments that they are in the expected values.

Example workflow: Check churn state, permanent hw address, actor system mac, speed, status and link failure count, aggregator id, and system mac address
    ./check_bonds.py --churn-state --permanent-hw-addr --actor-system-mac --speed 10000 --status both --aggregator-id --system-mac-addr /root/ci-fit/virtualenv/fusion-410/fusion/tests/wpst_crm/ci_fit/tools/appliance/d-nct/HA_ipaddr_I1_VPLagV5Woutnet_1_manual_correct_subnets_conflicts.conf

Author: Jason Mascarinas Pernito <jason.mas.pernito@hpe.com>

(c) Copyright 2018. Hewlett-Packard Enterprise
"""

import glob
import re
import argparse
import pprint
import sys
import os
import dmidecode
import time

# Attributes to check for a steady state:
# MII Status: up
# Speed: your bonding interface expected speed and that they all matched up
# Aggregator ID: consistent across all places
# System MAC address: icm3 connection MAC address
# details actor lacp pdu->system mac address: consistent with System MAC address
# Permanent HW addr: consistent with profile's icm3 and icm6 MAC address
# Actor Churn State: none
# Partner Churn State: none

# NOTE: When doing failover, Link Failure Count should increment

STATUS = None
SPEED = None
AGGR_ID = None
SYS_MAC = None
ACTOR_SYS_MAC = None
PERM_HW_ADDR = None
CHURN_STATE = None
LINK_FAILURE_COUNT = None
LINK_FAILURE_COUNT2 = None
RESET_LFCCACHE = None
PRINT_RUNNING_CONFIG = None
MULTI_TEST = None
HA_FILE = None
OS_WAIT_TIME = None


def get_dictionary_attribute(d, dk, errMsg='Default'):
    """
    Get dictionary attribute and raise KeyError if not found.
    Argument:
        d - dictionary
        dk - dictionary key
        errMsg - error message
    Return:
        value
    """
    try:
        return d[dk]
    except KeyError:
        if errMsg == 'Default':
            print '["%s" not found in %s] Exiting...' % (dk, d)
        else:
            print '[%s] Exiting...' % errMsg
        sys.exit(2)


def get_server_serial_number():
    """
    Get the server serial number using dmidecode.
    """
    key = 'Serial Number'
    for dsv in dmidecode.system().values():
        if key in dsv['data']:
            return dsv['data'][key]
    return None


def get_server_serial_number_data():
    """
    Get server serial number in the system is in your HA file.
    Raise an assertion error if serial number not found.
    Return: list of server HA data
    """
    server_ha_data = []
    # Production
    server_sn = get_server_serial_number().upper()
    # Eagle47 - for testing purposes mode=5
    # server_sn = 'VCUQQQ0005'
    # Eagle100 - for testing purposes mode=4
    # server_sn = 'VCUZZZ0011'
    with HA_FILE as h:
        for ha_line in h:
            ha = ha_line.split()
            # get all the data for the server
            if ha[8] == server_sn:
                server_ha_data.append(ha_line)
    if not server_ha_data:
        raise AssertionError('Unable to find server data from the HA file! '
                             'Check that serial number "%s" is in your HA file and try '
                             'again.' % server_sn)
    return server_ha_data


def get_server_unique_mac(ha_data_list):
    """
    Get server unique MAC address data from HA file.
    Argument:
        ha_data_list - list of HA file data
    Return: list of server unique mac data
    """
    server_unique_ha_data = []
    seen = {}
    for h in ha_data_list:
        ha = h.split()
        if ha[3] in seen:
            continue
        seen[ha[3]] = 1
        server_unique_ha_data.append(h)
    return server_unique_ha_data


def print_running_config(running_bonds_cfg):
    """
    Pretty print /proc/net/bonding/bond* in a dictionary data.
    """
    # construct PrettyPrinter instance
    pp = pprint.PrettyPrinter(indent=4)
    # print running config
    pp.pprint(running_bonds_cfg)


def _check_mii_status(subj_attr, npath, link_failure_count):
    """
    Check that MII Status are up.
    Check that Link Failure Count is as expected.
    Argument:
        subj_attr - dictionary of MII Status
        npath - path expected to be up
        link_failure_count - dictionary of Link Failure Count
    Return:
        0 - PASS
        1 - FAIL
    """
    mii_status_retval = 0
    skeys = sorted(subj_attr.keys())
    expected_status = {
        'both': {'overall': 'up', skeys[0]: 'up', skeys[1]: 'up', skeys[0] + '_lfc': 0, skeys[1] + '_lfc': 0},
        'icm3': {'overall': 'up', skeys[0]: 'up', skeys[1]: 'down', skeys[0] + '_lfc': 0, skeys[1] + '_lfc': 1},
        'icm6': {'overall': 'up', skeys[0]: 'down', skeys[1]: 'up', skeys[0] + '_lfc': 1, skeys[1] + '_lfc': 0}
    }
    failure_msg = []
    cache_dir = '/root/.lfccache'
    if not os.path.isdir(cache_dir):
        os.mkdir(cache_dir)
    for skey in skeys:
        if subj_attr[skey] != expected_status[npath][skey]:
            failure_msg.append('%s status is "%s"' % (skey, subj_attr[skey]))
        # get the link failure count from lfccache
        if skey == 'overall':
            continue
        if os.path.exists(cache_dir + '/' + skey):
            with open(cache_dir + '/' + skey) as c:
                expected_status[npath][skey + '_lfc'] = int(c.readline()) + expected_status[npath][skey + '_lfc']
            if int(link_failure_count[skey]) != int(expected_status[npath][skey + '_lfc']):
                failure_msg.append('%s link failure count %s(current) != %s(expected)' % (skey, link_failure_count[skey], expected_status[npath][skey + '_lfc']))
            else:
                with open(cache_dir + '/' + skey, 'w') as c:
                    c.write(link_failure_count[skey])
        else:
            sys.stdout.write('WARNING: No prior knowledge of the Link Failure Count, creating %s lfccache now...' % skey)
            try:
                with open(cache_dir + '/' + skey, 'w') as c:
                    c.write(link_failure_count[skey])
                    sys.stdout.write('OK ')
            except IOError:
                sys.stdout.write('[Failed: Unable to generate lfccache!]')
                mii_status_retval = 1
    if failure_msg:
        sys.stdout.write('[Failed: ')
        sys.stdout.write(', '.join(failure_msg))
        print '!]'
        mii_status_retval = 1
    else:
        print '[OK]'

    return mii_status_retval


def _filter_out_down_mii(subj_attr):
    """
    Filter out MII Status down.
    Argument:
        subj_attr - dictionary of MII Status.
    Return:
        Filtered subj_attr.
    """
    f_subj_attr = {}
    for fk, fv in subj_attr.iteritems():
        if fv != 'up':
            f_subj_attr[fk] = fv
    return f_subj_attr


def check_status(npath, bond_cfg):
    """
    Check that bonding interface status is up for the specified path.
    Check that link failure count is as expected.
    Argument:
        npath: This can be both|icm3|icm6
        bond_cfg - running bond config in dictionary
    Return:
        0 - PASS
        1 - FAIL
    """
    key = 'MII Status'
    lfc_key = 'Link Failure Count'
    status_retval = 0
    for sk, sv in bond_cfg.iteritems():
        sys.stdout.write('Checking %s path(s) in %s "%s" and "%s"...' % (npath, sk, key, lfc_key))
        # use dictionary to test consistency
        subj_attr = {}
        subj_attr['overall'] = sv[key]
        link_failure_count = {}
        for ss in sv['Slave Interface']:
            subj_attr[ss['Slave Interface']] = ss[key]
            link_failure_count[ss['Slave Interface']] = ss[lfc_key]
        status_retval = _check_mii_status(subj_attr, npath, link_failure_count)
    return status_retval


def check_speed(nspeed, bond_cfg):
    """
    Check that bonding interface speed is at the expected value.
    Argument:
        nspeed: Bonding interface speed (ie. 10000, 20000, etc)
        bond_cfg - running bond config in dictionary
    Return:
        0 - PASS
        1 - FAIL
    """
    key = 'Speed'
    speed_retval = 0
    for sp_k, sp_v in bond_cfg.iteritems():
        sys.stdout.write('Checking %s "%s"...' % (sp_k, key))
        failure_msg = []
        for sp_s in sp_v['Slave Interface']:
            if sp_s[key] != nspeed + ' Mbps':
                failure_msg.append('%s speed is "%s"' % (sp_s['Slave Interface'], sp_s[key]))
        if failure_msg:
            sys.stdout.write('[Failed: ')
            sys.stdout.write(', '.join(failure_msg))
            print '!]'
            speed_retval = 1
        else:
            print '[OK]'

    return speed_retval


def check_aggregator_id(bond_cfg):
    """
    Check that aggregator id is consistent.
    Argument:
        bond_cfg - running bond config in dictionary
    Return:
        1 - PASS
        0 - FAIL
    """
    key = 'Aggregator ID'
    aggr_retval = 0
    for ak, av in bond_cfg.iteritems():
        sys.stdout.write('Checking %s "%s"...' % (ak, key))
        # use dictionary to test consistency of aggregator id
        aggr_id = {}
        active_aggr_key = 'Active Aggregator Info'
        aggr_info_id = get_dictionary_attribute(av, active_aggr_key, errMsg='"%s" not found in %s!' % (active_aggr_key, ak))[key]
        if aggr_info_id not in aggr_id:
            aggr_id[aggr_info_id] = 1
        aggr_skip_messages = ['[Skipping: %s, Reason(s):' % key]
        for aggr_s in v['Slave Interface']:
            if aggr_s['MII Status'] == 'down':
                aggr_skip_messages.append(' MII Status is down for interface %s of %s]' % (aggr_s['Slave Interface'], ak))
                continue
            if aggr_s[key] not in aggr_id:
                aggr_id[aggr_s[key]] = 1
        if len(aggr_skip_messages) > 1:
            print "".join(aggr_skip_messages)
        elif len(aggr_id) != 1:
            print '[Failed: Aggregator IDs did not match!]' % ak
            aggr_retval = 1
        else:
            print "[OK]"
    return aggr_retval


def check_system_mac(bond_cfg, sys_mac_ha_data):
    """
    Check that system mac address is correct.
    Argument:
        bond_cfg - running bond config in dictionary
        sys_mac_ha_data - list of server data from HA file
    Return:
        1 - PASS
        0 - FAIL
    """
    test_key = 'System MAC address'
    sys_mac_retval = 0
    server_ha_data = get_server_unique_mac(sys_mac_ha_data)
    # should not be necessary but to make sure we are sorting HA data by MAC
    sorted(server_ha_data, key=lambda x: x.split()[3])
    # iterate over running config bonds
    for i in xrange(0, len(server_ha_data)):
        system_mac_bond = 'bond' + str(i)
        sys.stdout.write('Checking "%s" "%s"...' % (system_mac_bond, test_key))
        sys_mac = get_dictionary_attribute(bond_cfg[system_mac_bond], test_key, errMsg='"%s" not found in %s!' % (test_key, system_mac_bond))
        sys_mac = sys_mac.strip().upper()
        if server_ha_data[i].split()[3] == sys_mac:
            print '[OK]'
        else:
            print '[Failed: "%s" not expected!]' % sys_mac
            sys_mac_retval = 1
    return sys_mac_retval


def check_actor_sys_mac(bond_cfg):
    """
    Check that system mac address in details actor lacp pdu is correct.
    Argument:
        bond_cfg - running bond config in dictionary
    Return:
        1 - PASS
        0 - FAIL
    """
    pkey = 'details actor lacp pdu'
    key = 'system mac address'
    actor_sys_retval = 0
    for actor_sys_k, actor_sys_v in bond_cfg.iteritems():
        sys.stdout.write('Checking "%s" "%s"->"%s"...' % (actor_sys_k, pkey, key))
        # get the interface and system mac
        slave_interface = {}
        for actor_sys_s in actor_sys_v['Slave Interface']:
            interface = actor_sys_s['Slave Interface']
            slave_interface[interface] = get_dictionary_attribute(actor_sys_s, pkey, errMsg='"%s" not found in %s!' % (pkey, actor_sys_k))[key]
        macs = slave_interface.keys()
        if slave_interface[macs[0]] == slave_interface[macs[1]]:
            print '[OK]'
        else:
            print '[Failed: "%s"(%s) != "%s"(%s)!]' % (slave_interface[macs[0]], macs[0], slave_interface[macs[1]], macs[1])
            actor_sys_retval = 1

    return actor_sys_retval


def check_permanent_hw_addr(bond_cfg, hw_ha_data):
    """
    Check that the permanent hw address is consistent to HA file.
    Argument:
        bond_cfg - running bond config in dictionary
        hw_ha_data - list of server data from HA file
    Return:
        1 - PASS
        0 - FAIL
    """
    permanent_hw_retval = 0
    test_key = 'Permanent HW addr'
    server_ha_data = get_server_unique_mac(hw_ha_data)
    # should not be necessary but to make sure we are sorting HA data by MAC
    sorted(server_ha_data, key=lambda x: x.split()[3])
    # iterate over running config bonds
    for i in xrange(0, len(server_ha_data)):
        permanent_hw_bond = 'bond' + str(i)
        sys.stdout.write('Checking "%s" "%s"...' % (permanent_hw_bond, test_key))
        failure_msg = []
        # get the interface and permanent hw addr
        slave_interface = _get_slave_interface_attr(bond_cfg[permanent_hw_bond]['Slave Interface'], test_key, True, True)
        macs = sorted(slave_interface.keys())
        y = 1
        for x in xrange(0, len(macs)):
            y = y + 2
            if slave_interface[macs[x]] != server_ha_data[i].split()[y]:
                failure_msg.append('%s is not the expected MAC for "%s"' % (slave_interface[macs[x]], macs[x]))
        if failure_msg:
            sys.stdout.write('[Failed: ')
            sys.stdout.write(', '.join(failure_msg))
            print '!]'
            permanent_hw_retval = 1
        else:
            print '[OK]'

    return permanent_hw_retval


def _get_slave_interface_attr(slave_interface, attr, strip=False, upper=False):
    """
    Get a particular attribute from the Slave Interface list of dictionary data."
    Argument:
        slave_interface - Slave interface list of dictionary data
        attr - Attribute to retrieve
        strip - [Optional] Strip whitespaces
        upper - [Optional] Convert the string to all uppercase
    Return:
        Dictionary of bonding interface-attribute key-value pair.
    """
    filtered_slave_interface = {}
    for s_s in slave_interface:
        interface = s_s['Slave Interface']
        s_attr = get_dictionary_attribute(s_s, attr, errMsg='"%s" not found in %s!' % (attr, s_s))
        if strip:
            value = s_attr.strip()
        else:
            value = s_attr
        if upper:
            value = s_attr.upper()
        filtered_slave_interface[interface] = value
    return filtered_slave_interface


def check_churn_state(bond_cfg):
    """
    Check that actor and partner churn states are correct.
    Argument:
        bond_cfg - running bond config in dictionary
    Return:
        1 - PASS
        0 - FAIL
    """
    churn_retval = 0
    test_keys = ['Actor Churn State', 'Partner Churn State']
    for test_key in test_keys:
        expected_state = 'none'
        for churn_k, churn_v in bond_cfg.iteritems():
            sys.stdout.write('Checking "%s" "%s"...' % (churn_k, test_key))
            slave_interface = _get_slave_interface_attr(churn_v['Slave Interface'], test_key)
            keys = sorted(slave_interface.keys())
            failure_msg = []
            for key in keys:
                if slave_interface[key] != expected_state:
                    failure_msg.append('%s is not the expected "%s" for "%s"' % (slave_interface[key], test_key, key))
            if failure_msg:
                sys.stdout.write('[Failed: ')
                sys.stdout.write(', '.join(failure_msg))
                print '!]'
                churn_retval = 1
            else:
                print '[OK]'
    return churn_retval


def multi_ibs_multi_bonding_inspection(bond_cfg):
    """
    Perform multi ibs potash inspection based on the bonding mode and profile connection data.
    """
    multi_test_retval = 0
    cache_dir = '/root/.lfccache'
    if not os.path.isdir(cache_dir):
        os.mkdir(cache_dir)
    rhel = open('/etc/redhat-release', 'r').read().split(' ')[6].split('.')[0]
    for b, attrs in MULTI_TEST.expected_bonding_data.iteritems():
        sys.stdout.write('Searching bonding mode for %s...' % b)
        try:
            with open('/etc/sysconfig/network-scripts/ifcfg-' + b, 'r') as bconfigfile:
                for bconfig_line in bconfigfile:
                    if not re.match(r'BONDING_OPTS', bconfig_line):
                        continue
                    [_, _, bv] = bconfig_line.partition("=")
                    mode = bv.split(' ')[0].split('=')[1]
                    print '[OK]'
                    print 'Performing checks for bonding mode %s now...' % mode
        except IOError:
            print '[Failed: Unable to get bonding mode]'
            multi_test_retval = 1
        sys.stdout.write('Checking that overall bonding interface status is UP for %s...' % b)
        if 'MII Status' in attrs['ignoredAttributes']:
            print '[Skipping: MII Status]'
        else:
            if bond_cfg[b]['MII Status'] != 'up':
                print '[Failed]'
                multi_test_retval = 1
            else:
                print '[OK]'
        for slave_interface in bond_cfg[b]['Slave Interface']:
            # the rest of the modes: check link failure count, status, speed, and permanent hw addr is checked by default being the index key
            # check link failure count
            subject_slave_interface = slave_interface['Slave Interface']
            slave_interface_lfc = slave_interface['Link Failure Count']
            slave_interface_cache = cache_dir + '/' + subject_slave_interface
            if os.path.exists(slave_interface_cache):
                sys.stdout.write('Checking %s bonding interface Link Failure Count for %s...' % (subject_slave_interface, b))
                if 'Link Failure Count' in attrs['ignoredAttributes']:
                    print '[Skipping: Link Failure Count]'
                else:
                    with open(slave_interface_cache, 'r+') as c:
                        # entering check for link failure count
                        if attrs[slave_interface['Permanent HW addr'].upper()] == 'down':
                            # target found
                            expected_lfc = int(c.readline()) + 1
                        else:
                            # partner target
                            expected_lfc = int(c.readline())
                        if int(slave_interface_lfc) != expected_lfc:
                            print '[Failed: %s link failure count %s(current) != %s(expected)!]' % (subject_slave_interface, slave_interface_lfc, expected_lfc)
                            multi_test_retval = 1
                        else:
                            print '[OK]'
                            c.seek(0)
                            c.write(str(expected_lfc))
                            c.truncate()
            else:
                sys.stdout.write('WARNING: No prior knowledge of the Link Failure Count, creating %s lfccache now...' % subject_slave_interface)
                try:
                    with open(slave_interface_cache, 'w') as c:
                        c.write(slave_interface_lfc)
                        print '[OK]'
                except IOError:
                    print '[Failed: Unable to generate lfccache!]'
                    multi_test_retval = 1
            # check status
            expected_status = attrs[slave_interface['Permanent HW addr'].upper()]
            actual_status = slave_interface['MII Status']
            sys.stdout.write('Checking that %s bonding interface status is %s for %s...' % (subject_slave_interface, expected_status, b))
            if 'MII Status' in attrs['ignoredAttributes']:
                print '[Skipping: MII Status]'
            else:
                if expected_status != actual_status:
                    print '[Failed]'
                    multi_test_retval = 1
                else:
                    print '[OK]'
            # check flapping
            sys.stdout.write('Checking for network flapping in bonding interface %s for %s...' % (subject_slave_interface, b))
            multi_test_check_flapping = check_interface_status(subject_slave_interface, expected_status)
            if multi_test_check_flapping != 0:
                print '[Failed]'
                multi_test_retval = 1
            else:
                print '[OK]'
            # check speed
            expected_interface_speed = attrs['speed']
            actual_interface_speed = slave_interface['Speed']
            sys.stdout.write('Checking %s bonding interface speed for %s...' % (subject_slave_interface, b))
            if 'Speed' in attrs['ignoredAttributes']:
                print '[Skipping: Speed]'
            else:
                if actual_status == 'up' and actual_interface_speed == expected_interface_speed + ' Mbps':
                    print '[OK]'
                elif actual_status == 'down' and actual_interface_speed == 'Unknown':
                    print '[OK]'
                else:
                    print '[Failed: %s speed is "%s" while status is %s!]' % (subject_slave_interface, actual_interface_speed, actual_status)
            if mode == '4':
                # for bonding mode 4 checks the following: churn state (actor/partner), actor system mac, aggregator id, system mac addr
                # actor/partner churn state
                test_keys = ['Actor Churn State', 'Partner Churn State']
                expected_state = 'none'
                for test_key in test_keys:
                    if rhel == '6':
                        continue
                    sys.stdout.write('Checking %s bonding interface %s for %s...' % (subject_slave_interface, test_key, b))
                    if test_key in attrs['ignoredAttributes']:
                        print '[Skipping: %s]' % test_key
                    else:
                        if slave_interface[test_key] != expected_state:
                            print '[Failed: %s is not the expected "%s" for "%s"' % (slave_interface[test_key], test_key, subject_slave_interface)
                            multi_test_retval = 1
                        else:
                            print '[OK]'
        if mode == '4':
            # system mac address in details actor lacp pdu
            pkey = 'details actor lacp pdu'
            key = 'system mac address'
            sys.stdout.write('Checking "%s" "%s"->"%s"...' % (b, pkey, key))
            if pkey in attrs['ignoredAttributes']:
                print '[Skipping: %s]' % pkey
            elif key in attrs['ignoredAttributes']:
                print '[Skipping: %s]' % key
            else:
                # get the interface and system mac
                slave_interface = {}
                for ifs_s in bond_cfg[b]['Slave Interface']:
                    if rhel == '6':
                        continue
                    interface = ifs_s['Slave Interface']
                    slave_interface[interface] = get_dictionary_attribute(ifs_s, pkey, errMsg='"%s" not found in %s!' % (pkey, b))[key]
                macs = slave_interface.keys()
                if not slave_interface:
                    print '[Skipping: RHEL6.X has no %s]' % pkey
                elif slave_interface[macs[0]] != slave_interface[macs[1]]:
                    print '[Failed: "%s"(%s) != "%s"(%s)!]' % (slave_interface[macs[0]], macs[0], slave_interface[macs[1]], macs[1])
                    multi_test_retval = 1
                elif slave_interface[macs[0]] != bond_cfg[b]['System MAC address']:
                    print '[Failed: "%s"(%s) != "%s"(overall)!]' % (slave_interface[macs[0]], macs[0], bond_cfg[b]['System MAC address'])
                    multi_test_retval = 1
                elif slave_interface[macs[1]] != bond_cfg[b]['System MAC address']:
                    print '[Failed: "%s"(%s) != "%s"(overall)!]' % (slave_interface[macs[1]], macs[1], bond_cfg[b]['System MAC address'])
                    multi_test_retval = 1
                else:
                    print '[OK]'
            # aggregator id
            key = 'Aggregator ID'
            sys.stdout.write('Checking %s "%s"...' % (b, key))
            if key in attrs['ignoredAttributes']:
                print '[Skipping: %s]' % key
            elif 'Active Aggregator Info' in attrs['ignoredAttributes']:
                print '[Skipping: Active Aggregator Info]'
            else:
                # use dictionary to test consistency of aggregator id
                aggr_id = {}
                active_aggr_key = 'Active Aggregator Info'
                aggr_info_id = get_dictionary_attribute(bond_cfg[b], active_aggr_key, errMsg='"%s" not found in %s!' % (active_aggr_key, b))[key]
                if aggr_info_id not in aggr_id:
                    aggr_id[aggr_info_id] = 1
                skip_messages = ['[Skipping: %s, Reason(s):' % key]
                for aggr_id_s in bond_cfg[b]['Slave Interface']:
                    if aggr_id_s['MII Status'] == 'down':
                        skip_messages.append(' MII Status is down for interface %s of %s]' % (aggr_id_s['Slave Interface'], b))
                        continue
                    if aggr_id_s[key] not in aggr_id:
                        aggr_id[aggr_id_s[key]] = 1
                if len(skip_messages) > 1:
                    print "".join(skip_messages)
                elif len(aggr_id) != 1:
                    print '[Failed: Aggregator IDs did not match!]' % k
                    multi_test_retval = 1
                else:
                    print "[OK]"
            # system mac address should match with HA file/ha[3]
            key = 'System MAC address'
            sys.stdout.write('Checking that %s "%s" is as expected...' % (b, key))
            if rhel == '6':
                print '[Skipping: RHEL6.X has no %s]' % key
            elif key in attrs['ignoredAttributes']:
                print '[Skipping: %s]' % key
            elif bond_cfg[b][key] != attrs['System MAC address']:
                print '[Failed: %s %s != %s!]' % (b, bond_cfg[b][key], attrs['System MAC address'])
                multi_test_retval = 1
            else:
                print "[OK]"

    return multi_test_retval


def update_link_failure_count_cache(bond_cfg):
    """
    Update link failure count cache based on the bonding interface MII status in data file.
        bond_cfg - running bond config in dictionary
    """
    lfc_retval = 0
    cache_dir = '/root/.lfccache'
    if not os.path.isdir(cache_dir):
        os.mkdir(cache_dir)
    for lfc_b, attrs in LINK_FAILURE_COUNT2.expected_bonding_data.iteritems():
        for slave_interface in bond_cfg[lfc_b]['Slave Interface']:
            # ignore interfaces with status up
            if attrs[slave_interface['Permanent HW addr'].upper()] == 'up':
                continue
            subject_slave_interface = slave_interface['Slave Interface']
            slave_interface_lfc = slave_interface['Link Failure Count']
            slave_interface_cache = cache_dir + '/' + subject_slave_interface
            if os.path.exists(slave_interface_cache):
                sys.stdout.write('Updating %s bonding interface Link Failure Count cache for %s...' % (subject_slave_interface, lfc_b))
                try:
                    with open(slave_interface_cache, 'r+') as c:
                        expected_lfc = int(c.readline()) + 1
                        c.seek(0)
                        c.write(str(expected_lfc))
                        c.truncate()
                        print '[OK]'
                except IOError:
                    print '[Failed: Unable to update lfccache!]'
                    lfc_retval = 1
            else:
                sys.stdout.write('WARNING: No prior knowledge of the Link Failure Count, creating %s lfccache now...' % subject_slave_interface)
                try:
                    with open(slave_interface_cache, 'w') as c:
                        c.write(slave_interface_lfc)
                        print '[OK]'
                except IOError:
                    print '[Failed: Unable to generate lfccache!]'
                    lfc_retval = 1
    return lfc_retval


def reset_link_failure_count_cache(bond_cfg):
    """
    Reset link failure count cache based on the bonding interface name of MAC address in data file.
        bond_cfg - running bond config in dictionary
    """
    reset_lfc_retval = 0
    cache_dir = '/root/.lfccache'
    if not os.path.isdir(cache_dir):
        os.mkdir(cache_dir)
    for reset_lfc_b, _ in RESET_LFCCACHE.expected_bonding_data.iteritems():
        for slave_interface in bond_cfg[reset_lfc_b]['Slave Interface']:
            subject_slave_interface = slave_interface['Slave Interface']
            slave_interface_cache = cache_dir + '/' + subject_slave_interface
            sys.stdout.write('Resetting %s bonding interface Link Failure Count cache for %s...' % (subject_slave_interface, reset_lfc_b))
            try:
                with open(slave_interface_cache, 'w') as c:
                    c.write("0")
                    print '[OK]'
            except IOError:
                print '[Failed: Unable to reset lfccache!]'
                reset_lfc_retval = 1
    return reset_lfc_retval


def generate_link_failure_count(bond_cfg):
    """
    Generate link failure count cache.
        bond_cfg - running bond config in dictionary
    """
    gen_lfc_retval = 0
    test_key = 'Link Failure Count'
    cache_dir = '/root/.lfccache'
    if not os.path.isdir(cache_dir):
        os.mkdir(cache_dir)
    for _, gen_lfc_v in bond_cfg.iteritems():
        slave_interface = _get_slave_interface_attr(gen_lfc_v['Slave Interface'], test_key)
        for iface, lfcount in slave_interface.iteritems():
            sys.stdout.write('Generating "%s" cache for "%s"...' % (test_key, iface))
            cache_file = cache_dir + '/' + iface
            try:
                with open(cache_file, 'w') as c:
                    c.write(lfcount)
                    print '[OK]'
            except IOError:
                print '[Failed]'
                gen_lfc_retval = 1
    return gen_lfc_retval


# test dictionary
run_test = {
    'STATUS': check_status,
    'SPEED': check_speed,
    'AGGR_ID': check_aggregator_id,
    'SYS_MAC': check_system_mac,
    'ACTOR_SYS_MAC': check_actor_sys_mac,
    'PERM_HW_ADDR': check_permanent_hw_addr,
    'CHURN_STATE': check_churn_state,
    'LINK_FAILURE_COUNT': generate_link_failure_count,
    'PRINT_RUNNING_CONFIG': print_running_config,
}


def is_valid_file(parser, arg, mode='r'):
    """
       Test that arg is a valid file.
       Arguments:
           parser: parser object
           arg: file to test
       Return:
           an opened file arg
    """
    if not os.path.exists(arg):
        parser.error("The file %s does not exist!" % arg)
    else:
        return open(arg, mode)


def is_valid_data_file(parser, data_file):
    """
       Test that data_file is a valid data file.
       Arguments:
           parser: parser object
           data_file: file to test
       Return:
           imported data file
    """
    if not data_file:
        return data_file
    if not os.path.exists(data_file):
        parser.error("The file %s does not exist!" % data_file)
    else:
        import imp
        variableFileData = imp.load_source('variableFileData', data_file)
        return variableFileData


def check_interface_status(subject_slave_interface, expected_status):
    """
       Check the bonding interface status.
       Arguments:
           subject_slave_interface: Bonding slave interface name
           expected_status: expected status (up/down)
       Return:
           istatus_retval: interface status return value
    """
    istatus_retval = 0
    try:
        with open('/sys/class/net/' + subject_slave_interface + '/operstate', 'r') as c:
            x = c.readlines()
            for operstate_line in x:
                if str(operstate_line.strip("\n")) == str(expected_status.strip("\n")):
                    retval_flap = check_flapping(subject_slave_interface)
                    if retval_flap != 0:
                        istatus_retval = 1
                else:
                    istatus_retval = 1
    except IOError:
        print 'failed to get %s operstate...' % (subject_slave_interface)
    return istatus_retval


def grep_timestamp_logs(subject_slave_interface):
    """
       Grep for slave interface in varlog.
       Argument:
           subject_slave_interface: Bonding slave intername name
       Return:
           varlog line with interface and timestamp
    """
    path = '/root/.var_messages'
    localtime = time.asctime(time.localtime(time.time()))
    currenttime = localtime[4:19]
    time.sleep(int(OS_WAIT_TIME))
    var_log_cmd = "cat /var/log/messages|grep -i " + subject_slave_interface + " > " + path
    _ = os.system(var_log_cmd)
    with open(path) as fp:
        var = fp.readlines()
        j = 0
        for i in var:
            if currenttime in i:
                break
            else:
                j = j + 1
    return var[j:]


def check_flapping(subject_slave_interface):
    """
       Check for bonding interface flapping.
       Argument:
           subject_slave_interface: Bonding slave intername name
       Return:
           0: no flapping
           1: flapping was found
    """
    flap_retval = 0
    log_list = []
    temp = grep_timestamp_logs(subject_slave_interface)
    flag = 1
    for flap_line in temp:
        if re.search(r"NIC Link is", flap_line):
            log_list.append(flap_line)
    for lines in log_list:
        z = re.findall("NIC Link is Down", lines)
        if z == ['NIC Link is Down'] and flag == 1:
            continue
        else:
            flag = 2
            if z != ['NIC Link is Down']:
                flap_retval = 0
            else:
                flap_retval = 1
                break
    return flap_retval


def parseArguments():
    """
    Parse command line arguments and set global variables for it.
    **Parameters**:
         --status <Expected up bonding interface status: both|icm3|icm6>
         --speed <Expected bonding interface speed: 10000|20000>
         --aggregator-id <Check that aggregator id is consistent>
         --system-mac-addr <Check that system mac address is correct>
         --actor-system-mac <Check that system mac address in details actor lacp pdu is correct>
         --permanent-hw-addr <Check that permanent hw addr is consistent>
         --churn-state <Check that actor and partner churn state are correct>
         --cache-link-failure-count <Update link failure count cache>
         --print-running-config <Print running bonding interface config>
         --multi-test <Performs multiple checks based on bonding mode for a multi interconnect bay potash setup. Accepts data variable file containing expected profile bonding data.>
         <HA File>
    """
    global HA_FILE, MULTI_TEST, OS_WAIT_TIME, LINK_FAILURE_COUNT2, RESET_LFCCACHE

    parser = argparse.ArgumentParser(description="The script read the running bond files, convert the data into dictionary, and test that they are in the expected values.")
    parser.add_argument("--status", dest="STATUS", help="[Optional] Expected UP bonding interface status: both|icm3|icm6", default=STATUS, required=False, choices=['both', 'icm3', 'icm6'])
    parser.add_argument("--speed", dest="SPEED", help="[Optional] Expected bonding interface speed: 10000|20000", default=SPEED, required=False)
    parser.add_argument("--aggregator-id", action="store_true", dest="AGGR_ID", help="[Optional] Check that Aggregator ID is consistent", default=AGGR_ID, required=False)
    parser.add_argument("--system-mac-addr", action="store_true", dest="SYS_MAC", help="[Optional] Check that System MAC address is correct", default=SYS_MAC, required=False)
    parser.add_argument("--actor-system-mac", action="store_true", dest="ACTOR_SYS_MAC", help="[Optional] Check that system mac address in details actor lacp pdu is correct", default=ACTOR_SYS_MAC, required=False)
    parser.add_argument("--permanent-hw-addr", action="store_true", dest="PERM_HW_ADDR", help="[Optional] Check that permanent hw addr is consistent", default=PERM_HW_ADDR, required=False)
    parser.add_argument("--churn-state", action="store_true", dest="CHURN_STATE", help="[Optional] Check that actor and partner churn states are correct", default=CHURN_STATE, required=False)
    parser.add_argument("--cache-link-failure-count", action="store_true", dest="LINK_FAILURE_COUNT", help="[Optional] Create or update link failure count cache", default=LINK_FAILURE_COUNT, required=False)
    parser.add_argument("--update-link-failure-count", dest="LINK_FAILURE_COUNT2", help="[Optional] Update link failure count cache based on the profile bonding data file.", default=LINK_FAILURE_COUNT2, required=False)
    parser.add_argument("--reset-link-failure-count", dest="RESET_LFCCACHE", help="[Optional] Reset link failure count cache based on the profile bonding data file.", default=RESET_LFCCACHE, required=False)
    parser.add_argument("--print-running-config", action="store_true", dest="PRINT_RUNNING_CONFIG", help="[Optional] Print /proc/net/bonding/bond* in a dictionary data.", default=PRINT_RUNNING_CONFIG, required=False)
    parser.add_argument("--multi-test", dest="MULTI_TEST", help="[Optional] Performs multiple checks based on bonding mode for a multi interconnect bay potash setup. Accepts data variable file containing expected profile bonding data.", default=MULTI_TEST, required=False)
    parser.add_argument("ha-file", type=lambda x: is_valid_file(parser, x), help="[Required] HA File")
    parser.add_argument("--time", help="[Optional]The time to wait/sleep before starting the network flapping check. Since some operating systems takes longer than others to log the data. Accepts numeric value (e.g. 600 for 600 seconds).", dest="OS_WAIT_TIME", default=OS_WAIT_TIME, required=False)

    args = parser.parse_args()

    # remove ha-file from namespace
    HA_FILE = args.__dict__["ha-file"]
    del args.__dict__["ha-file"]
    MULTI_TEST = is_valid_data_file(parser, args.MULTI_TEST)
    LINK_FAILURE_COUNT2 = is_valid_data_file(parser, args.LINK_FAILURE_COUNT2)
    RESET_LFCCACHE = is_valid_data_file(parser, args.RESET_LFCCACHE)
    return args


if __name__ == "__main__":
    args_namespace = parseArguments()
    OS_WAIT_TIME = args_namespace.OS_WAIT_TIME

    # Production
    bonds = glob.glob("/proc/net/bonding/bond*")
    # Eagle100 - for testing purposes mode=4
    # bonds = glob.glob("/root/jasonp/e100_bonds/4/bond*")
    # Eagle47 - for testing purposes mode=5
    # bonds = glob.glob("/root/jasonp/e47_bonds/5/bond*")
    running_bonds = {}
    for bond in bonds:
        bond_num = bond.rpartition("/")[-1]
        running_bonds[bond_num] = {}
        top_attr = None
        slave_if = {}
        slave_if_started = 0
        with open(bond, "r") as bond_file:
            for line in bond_file:
                if not re.match(r'.*:.*', line):
                    continue
                [k, s, v] = line.partition(":")
                v = v.strip()
                pristine_k = k
                k = k.strip()
                if v.strip() == "":
                    top_attr = k
                    if slave_if_started:
                        slave_if[k] = {}
                    else:
                        running_bonds[bond_num][k] = {}
                else:
                    if top_attr and re.match("\s", pristine_k):
                        if slave_if_started:
                            slave_if[top_attr][k] = v
                        else:
                            running_bonds[bond_num][top_attr][k] = v
                    elif k == "Slave Interface" or slave_if_started:
                        if k in slave_if:
                            running_bonds[bond_num][k] = [slave_if]
                            slave_if = {}
                            slave_if[k] = v
                        else:
                            # start creating new dictionary for slave interface
                            slave_if[k] = v
                            slave_if_started = 1
                            top_attr = None
                    else:
                        running_bonds[bond_num][k] = v
            running_bonds[bond_num]["Slave Interface"].append(slave_if)

    ha_data = get_server_serial_number_data()
    # perform test(s)
    retval = 0
    tmp_retval = 0
    if MULTI_TEST:
        # perform multi test, ignore the individual tests
        retval = multi_ibs_multi_bonding_inspection(running_bonds)
    elif LINK_FAILURE_COUNT2:
        # perform update on link failure count cache based on data file status bond interface status
        retval = update_link_failure_count_cache(running_bonds)
    elif RESET_LFCCACHE:
        # reset link failure count cache
        retval = reset_link_failure_count_cache(running_bonds)
    else:
        for k in args_namespace.__dict__:
            farg = args_namespace.__dict__[k]
            if (isinstance(farg, bool) and farg is not True) or farg is None:
                continue
            if k == "PRINT_RUNNING_CONFIG":
                run_test[k](running_bonds)
            elif k in ["CHURN_STATE", "LINK_FAILURE_COUNT", "AGGR_ID", "ACTOR_SYS_MAC"]:
                tmp_retval = run_test[k](running_bonds)
            elif isinstance(farg, bool):
                tmp_retval = run_test[k](running_bonds, ha_data)
            else:
                tmp_retval = run_test[k](farg, running_bonds)
            if tmp_retval and not retval:
                retval = tmp_retval
    sys.exit(retval)
