# (C) Copyright 2013 Hewlett-Packard Development Company, L.P.
""" HP iLO CLI client """
from hpilo import Ilo, IloWarning, IloLoginFailed, IloError
import re
import socket
import sys
import warnings

try:
    import xml.etree.ElementTree as etree
except ImportError:
    import elementtree.ElementTree as etree

PY3 = sys.version_info[0] >= 3
if PY3:
    import urllib.request as urllib2
    import io as StringIO
    b = lambda x: bytes(x, 'ascii')

    class Bogus(Exception):
        pass

    socket.sslerror = Bogus
    basestring = str
else:
    import urllib2
    import cStringIO as StringIO
    b = lambda x: x


class IloClient(Ilo):

    def __init__(self, hostname, login=None, password=None, timeout=60, port=443, protocol=None, delayed=False):
        super(IloClient, self).__init__(hostname, login, password, timeout, port, protocol, delayed)

    def _element_children_to_dict(self, element):
        """[Override] Returns a dict with tag names of all child elements as keys and the
           VALUE attributes as values"""
        retval = {}
        keys = [elt.tag.lower() for elt in element]
        if len(keys) != 1 and len(set(keys)) == 1:
            # Can't return a dict
            retval = []

        for elt in element:
            # There are some special tags
            fname = '_parse_%s_%s' % (element.tag.lower(), elt.tag.lower())
            if hasattr(self, fname):
                retval.update(getattr(self, fname)(elt))
                continue
            key, val, unit = elt.tag.lower(), elt.get('VALUE', elt.get('value', None)), elt.get('UNIT', None)
            if val is None:
                # HP is not best friends with consistency. Sometimes there are
                # attributes, sometimes child tags and sometimes text nodes. Oh
                # well, deal with it :)
                if elt.tag == "SSO_SERVER":  # we must not eliminate attributes of SSO_SERVER node
                    if elt.attrib:
                        val = self._element_to_dict(elt)
                        val['$text$'] = elt.text.strip()
                        val = [val]
                else:
                    if elt.attrib and list(elt):
                        val = self._element_to_dict(elt)
                    elif list(elt):
                        val = self._element_to_list(elt)
                    elif elt.text:
                        val = elt.text.strip()
                    elif elt.attrib:
                        val = self._element_to_dict(elt)

            val = self._coerce(val)

            if unit:
                val = (val, unit)
            if isinstance(retval, list):
                retval.append(val)
            elif key in retval:
                if isinstance(retval[key], dict):
                    retval[key].update(val)
                elif not isinstance(retval[key], list):
                    retval[key] = [retval[key], val]
                else:
                    retval[key].append(val)
            else:
                retval[key] = val
        return retval

    def delete_sso_cert_by_index(self, sso_idx):
        """Delete the sso server by index from the ilo"""
        return self._control_tag('SSO_INFO', 'DELETE_SERVER', attrib={'INDEX': '%s' % sso_idx})

    def delete_all_sso_certs(self):
        """Delete all sso server from the ilo"""
        sso_setting = self.get_sso_settings()
        sso_servers = sso_setting.get('sso_server', None)
        if sso_servers is not None:
            for server in sso_servers:
                self.delete_sso_cert_by_index(server['index'])
