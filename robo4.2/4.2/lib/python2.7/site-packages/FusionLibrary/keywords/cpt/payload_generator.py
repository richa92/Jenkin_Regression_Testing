#!/usr/bin/env python27
# (C) Copyright 2018 Hewlett Packard Enterprise Development LP
"""
Keywords for generating payload that is required by L2AddKeywords in RG
"""
from functools import wraps
from robot.api.deco import keyword
from RoboGalaxyLibrary.utilitylib import logging
from socket import inet_aton


def skip_method(func):
    """
    Decorator to skip internal methods
    :param func: handler to the internal method
    :return:
    """
    @wraps(func)
    def wrap(self, *args, **kwargs):
        """
        The wrapper
        :param self: The class object itself
        :param args: vargs
        :param kwargs: heyword args
        :return: what the method returns
        """
        if self.filter:
            return None
        else:
            return func(self, *args, **kwargs)

    return wrap


class CptPayloadGenerator(object):
    """
    Custom keyword class for generating request payloads to be used for OS
    deployment with Cirrus Provisioning Tool
    """
    def __init__(self):
        """Class initialization method"""
        self.server = None
        self.filter = False

    def _set_server_profile(self, uri):
        """
        Configures the Object attribute profile with information received
        :param uri: (String) URI
        :return: None
        """
        # Workaround of not being an object for the keywords
        # Fixme: Modularize the keywords
        self.filter = False
        self.server = self.fusion_api_get_server_profiles(uri=uri)

        if self.server['status_code'] != 200:
            # Reset variable to None due to lack of information
            self.server = None
            logging.info("{} is invalid.".format(uri))
            self.filter = True
            return None

        if self.server.get('status') == "Critical" and \
                self.server.get('state') != "Normal":
            _ = "{} is reporting {} status.".format(self.server.get('name'),
                                                    self.server.get('status'))
            logging.info(_)
            self.filter = True
            return None

    def _get_os_profile_dict(self, body, bulk=False):
        """
        Returns the JSON object after processing the initial input from
        :param body: JSON object
        :param bulk: (Boolean) Flag for bulk provisioning
        :return: DICT holding OS profile information
        """
        required_attrs = ['os_name', 'os_repo', 'deployment_network',
                          'ilo_user', 'ilo_pass']

        if not set(required_attrs).issubset(body.keys()):
            m = "Missing required attributes."
            m += "\nRequired attributes are {}".format(required_attrs)
            m += "\nFound attributes are {}".format(body.keys())
            logging.info(m)
            self.filter = True
            return None

        rst = {'os_name': body.get('os_name'),
               'os_repo': body.get('os_repo'),
               'kickstart': body.get('kickstart', ''),
               'custom_script': body.get('custom_script', ''),
               'spp': body.get('spp', '')}

        if bulk:
            rst['storage_driver'] = body.get('storage_driver', '')
            rst['network_driver'] = body.get('network_driver', '')
        else:
            rst['storage'] = {"drivers": body.get('storage_driver', '')}
            rst['network'] = {"drivers": body.get('network_driver', '')}

        return rst

    @skip_method
    def _get_host_dict(self, body):
        """
        Configures the host information for deployment
        :param body: JSON dict provided by the user
        :return: JSON dict holding host (name, password)
        """
        return {'name': body.get('hostname', self.server['serialNumber']),
                'password': body.get('system_password', 'HPvse123$')}

    @skip_method
    def _get_boot_mode(self):
        """
        Configures the server's boot mode
        :return: (String) Legacy | UEFI
        """
        if self.server.get('bootMode') and \
                self.server.get('bootMode').get('mode') != "BIOS":
            return "UEFI"
        else:
            return "Legacy"

    @skip_method
    def _get_network_uri(self, net):
        """
        Returns the URI of the network\network set
        :param net: (String) name of the network\network set
        :return: (String) URI
        """
        p = '?&filter="\'name\'==\'{}\'"'.format(net)
        r = self.fusion_api_get_ethernet_networks(param=p)

        if r['count'] == 0:
            #  check for networkset
            r = self.fusion_api_get_network_set(param=p)
            if r['count'] == 0:
                m = "Unable to find {} network/network set.".format(net)
                m += "Please provide the right deployment ethernet network/network set"
                logging.info(m)
                self.filter = True
                return
        elif r['count'] > 1:
            m = "Something went wrong. Unable to retrieve {} URI".format(net)
            logging.info(m)
            self.filter = True
            return

        return r['members'][0]['uri']

    @skip_method
    def _get_net_dict(self, net):
        """
        Returns the DICT containing network details required for deployment
        :param net: (String) name of the network
        :return: JSON dict containing mac, pos
        """
        uri = self._get_network_uri(net)
        # ServerProfileV7 and below don't have connectionSettings
        # In case of upgrade test cases.
        if int(self.server.get('type').split('V')[1]) < 8:
            con = self.server.get('connections', [])
        else:
            con = self.server['connectionSettings'].get('connections')

        nets = sorted(con, key=lambda p: p['id'])

        for c, k in enumerate(nets):
            if k['networkUri'] == uri:
                return {'mac': k['mac'], 'pos': c + 1}

        m = "Server profile {} did not contain ".format(self.server.get('name'))
        m += "deployment network connection {}".format(net)
        logging.info(m)
        self.filter = True

    def _get_lun_id(self):
        """
        Returns the LUN UUID of the boot volume. The keys in volumeAttachments
        under 'sanStorage' that determine boot volume status are 'isBootVolume'
        or 'bootVolumePriority' --> Primary. By default, the LUN ID returned
        would be DYNAMIC
        :return str: LUN UUID
        """
        vol_uri = None

        for v in self.server['sanStorage'].get('volumeAttachments', list()):
            # Boot volume is determined by bootVolumePriority in V10
            if v.get('isBootVolume', False) or \
                    v.get('bootVolumePriority', str()) == 'Primary':
                vol_uri = v.get('volumeUri')
                break

        if vol_uri:
            _id = self.fusion_api_get_storage_volumes(uri=vol_uri).get('lunWwn')
            # LUN WWN can be None
            return _id.replace(':', '') if _id else 'DYNAMIC'
        else:
            return 'DYNAMIC'

    @skip_method
    def _get_storage_dict(self):
        """
        Returns the DICT containing storage details like multipath, fcoe & LUN
        :return: JSON dict
        """
        san_path = 0
        fcoe_dict = dict()
        rst = dict()
        if int(self.server.get('type').split('V')[-1]) < 8:
            con = self.server.get('connections', [])
        else:
            con = self.server['connectionSettings'].get('connections', [])

        for i in sorted(con, key=lambda c: c['id']):
            if i.get('boot'):
                if i.get('boot').get('priority') != "NotBootable":
                    san_path += 1

                    # Additional inputs are required for FCoE & iSCSI
                    if 'fcoe-networks' in i.get('networkUri'):
                        fcoe_dict['enabled'] = True
                        if i.get('boot').get('priority') == "Primary":
                            fcoe_dict['mac1'] = i.get('mac')
                        elif i.get('boot').get('priority') == "Secondary":
                            fcoe_dict['mac2'] = i.get('mac')

                    if i['boot'].get('ethernetBootType') == 'iSCSI':
                        rst['iSCSI'] = True

        if fcoe_dict:
            rst['fcoe'] = fcoe_dict

        if san_path > 1:
            rst['multipath'] = True

        if san_path >= 1:
            rst['lun_id'] = self._get_lun_id()

        return rst

    @skip_method
    def _get_ilo_dict(self, ilo_user, ilo_pass):
        """
        Returns the iLO dictionary for CPT input file
        :param ilo_user: iLO Username
        :param ilo_pass: Password for Username
        :return: JSON dict of iLO block
        """
        u = self.server['serverHardwareUri']
        r = self.fusion_api_get_server_hardware(uri=u)

        if not r:
            m = "Unable to retrieve server hardware information from profile."
            m += "Profile: {}\nHardware URI {}".format(self.server['name'], u)
            logging.info(m)
            self.filter = True
            return None

        rst = dict()
        for n in r.get('mpHostInfo', '').get('mpIpAddresses'):
            logging.debug("iLO address: {}".format(n.get('address')))
            try:
                # inet_aton supports only IPv4 addressing which is on the lines
                # of CPT
                if inet_aton(n.get('address')):
                    rst['ip'] = n.get('address')
                    break
            except:
                continue

        if not rst.get('ip'):
            m = "Unable to retrieve the iLO IPv4 address for the server."
            logging.info(m)
            self.filter = True
            return None

        # Fixme: Retrieve iLO credentials from OneView rather forcing the user
        # to pass this information
        rst['user'] = ilo_user
        rst['password'] = ilo_pass

        return rst

    @keyword(name="Create CPT Payload For OS Deployment")
    def generate_payload(self, server_uri, body):
        """
        Helper method for generating the request body required by CPT Deploy OS
        :param server_uri: URI of the server to be provisioned
        :param body: JSON Object containing OS profile information
        :return: JSON Object
        """
        self._set_server_profile(server_uri)
        if not self.server:
            logging.debug("{} has been discarded.".format(server_uri))
            raise AssertionError('Unable to create payload.')

        b = self._get_os_profile_dict(body)
        b['host'] = self._get_host_dict(body)
        b['boot_mode'] = self._get_boot_mode()
        b['network'].update(self._get_net_dict(body.get('deployment_network')))
        b['storage'].update(self._get_storage_dict())
        b['ilo'] = self._get_ilo_dict(body.get('ilo_user'),
                                      body.get('ilo_pass'))

        if self.filter:
            logging.info("Server profile at {} is discarded".format(server_uri))
            raise AssertionError('Unable to create payload.')

        logging.debug("Input for CPT:\n {}".format(b))

        return b

    @keyword(name="Create CPT Payload For Bulk OS Deployment")
    def bulk_deployment(self, items):
        """
        Helper method for generating the request body required by CPT Deploy OS.
        It expects nodes to be a type of (server_uri, body)
        :param items: List of tuples containing server_uri & os profile
        :return: JSON Object for bulk provisioning
        """
        oses = list()
        nodes = list()
        for server_uri, body in items:
            self._set_server_profile(server_uri)
            # Server URI is unique however Profile may not be so
            os = self._get_os_profile_dict(body, bulk=True)

            if self.filter:
                m = "Server profile at {} is discarded ".format(server_uri)
                m += "due to an issue with OS profile."
                logging.info(m)
                # There is no point in adding the node
                continue

            node = {'host': self._get_host_dict(body),
                    'boot_mode': self._get_boot_mode(),
                    'network': self._get_net_dict(body['deployment_network']),
                    'storage': self._get_storage_dict(),
                    'ilo': self._get_ilo_dict(body.get('ilo_user'),
                                              body.get('ilo_pass')),
                    'os_profile': body.get('os_name')}

            if self.filter:
                m = "Server profile at {} is discarded. ".format(server_uri)
                m += "Encountered a problem in retrieving hardware information."
                logging.info(m)
                # No point in adding profile and node
                continue

            nodes.append(node)
            if len(oses) == 0:
                oses.append(os)
            else:
                if os['os_name'] not in map(lambda x: x['os_name'], oses):
                    oses.append(os)

        if not len(oses):
            raise AssertionError('Unable to create payload.')

        rst = {'os': oses, 'nodes': nodes}
        logging.debug("Input for CPT:\n {}".format(rst))

        return rst
