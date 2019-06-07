#!/usr/bin/env python27
# (C) Copyright 2018 Hewlett Packard Enterprise Development LP
"""
Custom keyword that generators the required payload for Configure OS Networks
keyword.
"""
from copy import deepcopy
from RoboGalaxyLibrary.utilitylib.logging import logger as log
from robot.api.deco import keyword


class NetworkConfigGenerator(object):
    """
    Custom keyword that generates the payload for Configure OS Network
    """
    def __init__(self):
        """
        Object initializer... holds the profile information of the server
        """
        self.net_profile = dict()
        self.ports = dict()
        self.body = dict({'host': dict(), 'config': list()})

    def _set_ports(self, cons):
        """
        Assigns the ports information based on the information from the server
        profile's connections
        :param list cons: List of connections
        :return: None
        """
        for port in cons:
            if port.get('type', port.get('functionType')).lower() == 'ethernet':
                if port.get('networkUri') in self.ports:
                    self.ports[port['networkUri']].append(port.get('mac'))
                else:
                    self.ports.update({port['networkUri']: [port['mac']]})

    def _validate_and_set_host(self, host):
        """
        Verifies and adds the target information to the body
        :param dict host: Contains
        :return bool: True if the payload is updated with host information
        """
        attrs = ['ipv4', 'user', 'password']

        if not host.get('os'):
            log.debug('Missing required attribute: os')
            return False

        if not set(attrs).issubset(host.keys()):
            m = 'Found attributes: {}'.format(host.keys())
            m += '\nRequired attributes: {}'.format(attrs)
            log.info(m)
            return False

        if host.get('datacenter'):
            if host.get('manager') is None:
                log.info('Missing required attribute: manager')
                return False

        self.body['host'] = deepcopy(host)
        log.debug('Host information found {}'.format(host))
        return True

    def _get_network_uri(self, name):
        """
        Retrieve the networkUri from OneView based on the argument
        :param str name: Network name
        :return str: Network's URI corresponding to OV
        """
        p = '?&filter="\'name\'==\'{}\'"'.format(name.lower())
        r = self.fusion_api_get_ethernet_networks(param=p)

        if r.get('count') == 0:
            r = self.fusion_api_get_network_set(param=p)
            if r.get('count') == 0:
                log.info('{} not found in OneView'.format(name))
                return None

        if r.get('count') > 1:
            log.info('Found more than one match for {}'.format(name))
            return None

        log.debug('Retrieved the network uri for {}'.format(name))
        return r.get('members')[0]['uri']

    def _get_network_addr(self, uri, vmware=False):
        """
        Returns a dictionary that holds config['networks'] entry
        :param str uri: OneView network information
        :param bool vmware: If the requestor is vmware
        :return dict: config['networks'] dictionary
        """
        n = self.fusion_api_get_ethernet_networks(uri=uri)
        if n is None:
            log.debug('No network information for {}'.format(uri))
            return None

        b = dict({'dhcp': True,
                  'vlan': n.get('vlanId')})

        if vmware:
            b.update({'name': n['name'],
                      'type': n.get('purpose')})

        # DHCP is set till the method is able to allocate an IP address
        if n.get('subnetUri', None) is None:
            log.debug('No associated network for {}'.format(uri))
            return b

        s = self.fusion_api_get_ipv4_subnet(uri=n.get('subnetUri'))
        if s is None:
            log.debug('No subnet information for {}'.format(n['subnetUri']))
            return b

        a = self.fusion_api_allocate_ipv4_subnet({'count': 1}, s['uri'])
        if a.get('status_code') != 200:
            log.debug('No available IPv4 address.')
            return b

        b['dhcp'] = False
        b.update({'ipv4': a['idList'][0], 'netmask': s['subnetmask']})

        return b

    def _add_rhel_config(self, name, uri):
        """
        Creates the network configuration for RHEL based systems
        :param str name: Name of the network name
        :param str uri: OneView's networkUri
        :return bool: True when network configuration is appended to body
        """
        port_count = len(self.ports[uri])
        if self.net_profile['type'].lower() == 'ethernet' and port_count != 1:
            _ = 'Invalid number of ports {}'.format(name)
            log.info(_)
            return False

        if (self.net_profile['type'].lower() == 'bond' or
            self.net_profile['type'].lower() == 'team') and \
                port_count != 2:
            _ = 'Invalid number of port for {}'.format(name)
            log.info(_)
            return False

        cfg = {'name': self.net_profile.get('name', name),
               'type': self.net_profile['type'],
               'ports': self.ports[uri]}

        if self.net_profile['type'].lower() == 'bond':
            cfg.update({'bond_opts': self.net_profile['bond_opts']})
        elif self.net_profile['type'].lower() == 'team':
            cfg.update({'team_opts': self.net_profile['team_opts'],
                        'team_port_cfg': self.net_profile['team_port_cfg']})

        nets = list()
        if 'ethernet-network' in uri:
            n = self._get_network_addr(uri)
            if n is not None:
                # VLAN is configured on the interconnect
                if n.get('vlan'):
                    # Removing VLAN as it is a single network and Oneview
                    # configures the same on the interconnect downlink port
                    del n['vlan']

                nets.append(n)
        elif 'network-set' in uri:
            r = self.fusion_api_get_network_set(uri=uri)
            if r.get('nativeNetworkUri'):
                n = self._get_network_addr(r['nativeNetworkUri'])
                if n is not None:
                    if n.get('vlan'):
                        # Removing VLAN as it is native to network set and
                        # configured by Oneview on the interconnect downlink
                        del n['vlan']

                    nets.append(n)

            for u in r.get('networkUris', []):
                if u == r.get('nativeNetworkUri'):
                    log.debug('Ignoring this network as it is native')
                    continue

                n = self._get_network_addr(u)
                if n is not None:
                    nets.append(n)
        else:
            log.info('Unknown OneView network connection: {}'.format(uri))
            log.info('Supported types: ethernet, network-set')
            return False

        if nets:
            cfg['networks'] = deepcopy(nets)
            self.body['config'].append(cfg)
            log.debug('Network config: {}'.format(cfg))
            return True

        log.debug('No network information retrieved... skipping')
        return False

    def _add_vmware_config(self, uri):
        """
        Creates the network configuration for VMware based systems
        :param str uri: OneView's networkUri
        :return bool: True when network configuration is appended to body
        """
        if self.net_profile.get('name') is None:
            log.info('Virtual Switch name is required')
            return False

        if self.net_profile.get('type').lower() == 'vds':
            attrs = ['manager', 'datacenter', 'cluster']

            if not set(attrs).issubset(self.body['host'].keys()):
                m = 'Missing required attributes.'
                m += "Additional required attributes are\t{}".format(attrs)
                log.info(m)
                return False

        cfg = dict({'name': self.net_profile['name'],
                    'type': self.net_profile['type'],
                    'ports': self.ports[uri]})

        nets = list()
        if 'ethernet-network' in uri:
            n = self._get_network_addr(uri, True)
            if n is None:
                return False

            if self.net_profile.get('networks') and \
                    self.net_profile['networks'].get(n['vlan']):
                if 'policy' in self.net_profile['networks'][n['vlan']]:
                    n['policy'] = \
                        self.net_profile['network'][n['vlan']]['policy']

                if 'vmk' in self.net_profile['network'][n['vlan']]:
                    n['vmk'] = self.net_profile['network'][n['vlan']]['vmk']
                else:
                    # No vmkernel port would be created
                    n['vmk'] = False
            else:
                n['vmk'] = False

            # VLAN is configured on the downlink port
            del n['vlan']
            nets.append(n)
        elif 'network-set' in uri:
            ns = self.fusion_api_get_network_set(uri=uri)
            if ns.get('nativeNetworkUri'):
                n = self._get_network_addr(ns['nativeNetworkUri'], True)
                if n is not None:
                    if self.net_profile.get('networks') and \
                            self.net_profile['networks'].get(n['vlan']):
                        if 'policy' in self.net_profile['networks'][n['vlan']]:
                            n['policy'] = \
                                self.net_profile['networks'][n['vlan']]['policy']

                        if 'vmk' in self.net_profile['networks'][n['vlan']]:
                            n['vmk'] = \
                                self.net_profile['networks'][n['vlan']]['vmk']
                        else:
                            n['vmk'] = False
                    else:
                        n['vmk'] = False

                    del n['vlan']
                    nets.append(n)

            for u in ns.get('networkUris', []):
                if u == ns.get('nativeNetworkUri'):
                    log.debug('Ignoring this network as it is a native one.')
                    continue

                n = self._get_network_addr(u, True)
                if n is None:
                    continue

                if self.net_profile.get('networks') and \
                        self.net_profile['networks'].get(n['vlan']):
                    if 'policy' in self.net_profile['networks'][n['vlan']]:
                        n['policy'] = \
                            self.net_profile['networks'][n['vlan']]['policy']

                    if 'vmk' in self.net_profile['networks'][n['vlan']]:
                        n['vmk'] = \
                            self.net_profile['networks'][n['vlan']]['vmk']
                    else:
                        n['vmk'] = False
                else:
                    n['vmk'] = False

                nets.append(n)

            cfg['active'] = self.net_profile.get('active', len(cfg['ports']))
        else:
            log.info('Unsupported network connection {}'.format(uri))
            log.info('Supported types: vss, vds')

        if nets:
            cfg['networks'] = nets
            self.body['config'].append(cfg)
            log.debug('Network config: {}'.format(cfg))
            return True

        log.debug('No network information was retrieved... skipping')
        return False

    def _add_network_profile(self, net_profile):
        """
        In conjunction with ports, creates the configuration dictionary
        :param dict net_profile: Network profile information
        :return bool: True when the configuration is added to self.body
        """
        net_types = list()

        if 'redhat' in self.body['host']['os'].lower() or \
                'red hat' in self.body['host']['os'] or \
                'rhel' in self.body['host']['os']:
            net_types = ['ethernet', 'bond', 'team']
        elif 'vmware' in self.body['host']['os'].lower():
            net_types = ['vss', 'vds']

        if not net_profile.get('type') or \
                not net_profile['type'].lower() in net_types:
            log.info('Unknown network config: {}'.format(net_profile['type']))
            log.info('Supported network configurations: {}'.format(net_types))
            return False

        net_uri = self._get_network_uri(net_profile.get('ov_network'))
        if net_uri is None:
            return False

        if net_uri not in self.ports:
            log.info('Network not part of server profile connections {}')
            return False

        self.net_profile = deepcopy(net_profile)

        if 'redhat' in self.body['host']['os'].lower() or \
                'red hat' in self.body['host']['os'] or \
                'rhel' in self.body['host']['os']:
            return self._add_rhel_config(net_profile['ov_network'], net_uri)
        elif 'vmware' in self.body['host']['os'].lower():
            return self._add_vmware_config(net_uri)

        log.debug('Unknown network profile type {}'.format(net_profile['type']))
        return False

    @keyword(name='Create Payload For OS Networks Configuration')
    def _network_config_generator(self, sp_url, host_info, nets):
        """
        Keyword to generate the required payload for configuring the target
        system networks

        Usage
          ${body}=    Create Payload For OS Networks Configuration |
          ...             <ov_server_profile_url> |
          ...             <host_info> |
          ...             <network_profiles> |

        [Returns]
          A dictionary which would be an input to 'Configure OS Networks'

        :param str sp_url: Target system's OneView server profile URL
        :param dict host_info: Target system's credentials and type
        :param list nets: List of network profiles
        :return:
        """
        sp = self.fusion_api_get_server_profiles(uri=sp_url)

        if sp['status_code'] != 200:
            log.info("Invalid OneView Server Profile URL: {}".format(sp_url))
            return self.body

        if int(sp['type'].split('V')[-1]) < 8:
            self._set_ports(sp.get('connections', list()))
        else:
            self._set_ports(sp.get('connectionSettings').get('connections'))

        if not self._validate_and_set_host(host_info):
            log.info("Invalid target server information: {}".format(host_info))
            return self.body

        for net in nets:
            if self._add_network_profile(net):
                log.debug('{} network configuration created.'.format(net))

        return self.body if len(self.body['config']) else dict()
