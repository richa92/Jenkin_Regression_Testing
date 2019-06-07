import json
from RoboGalaxyLibrary.utilitylib import logging as logger
import re


class InterconnectRoleAndFwVersionValidate(object):

    def make_li_spp_body(self, command=None, ethernetActivationDelay=None, ethernetActivationType=None, force=None, sppUri=None,):
        body = {'command': command, 'ethernetActivationDelay': ethernetActivationDelay, 'ethernetActivationType': ethernetActivationType, 'force': force, 'sppUri': sppUri, }
        return body

    def get_potash_firmware_version(self, Potash_Version=None):
        searchObj = re.search(r'ESS ([0-9][0-9][0-9][0-9])', Potash_Version, re.M | re.I)
        return searchObj.group(1)

    def get_hfpotash_firmware_version(self, Potash_Version=None):
        return Potash_Version.split()[0].replace('-', '.')

    def get_chloride_firmware_version(self, Chloride_Version=None):
        searchObj = re.search(r'Firmware(.*)0\.[0-9][0-9]', Chloride_Version, re.M | re.I)
        return searchObj.group().split(':')[1].strip()

    def get_potash_irf_member_role(self, Potash_irf_member_role=None):
        searchObj = re.search(r'(.*)\+(.*)', Potash_irf_member_role, re.M | re.I)
        return searchObj.group(0).split()[1]

    def get_hfpotash_irf_member_role(self, Potash_irf_member_role=None):
        searchObj = re.search(r'(Node.* State.*)', Potash_irf_member_role, re.M | re.I)
        if searchObj.group(0).split(':')[1].strip() == "Active":
            return "Master"
        else:
            return "Subordinate"
