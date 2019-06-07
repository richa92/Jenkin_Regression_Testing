""" DCS API Keywords """
import json
from FusionLibrary.api.common.request import HttpVerbs


class DCSAPIKeywords(object):
    """ DCS API Keywords """
    def __init__(self):
        self.dcs_fusion_client = HttpVerbs()

    def dcs_api_get_status(self, fusion_ip):
        """
        Return the status of the DCS.
        | ${resource} | DCS Api Get Status  | <fusion_ip> |
        """
        uri = 'http://%s:9990/dcs/rest/schematic/dcs_status' % fusion_ip
        return self.dcs_fusion_client.get(uri)

    def dcs_api_get_instances(self, fusion_ip):
        """
        Return the instances of the DCS.
        | ${resource} | DCS Api Get Instances  | <fusion_ip> |
        """
        uri = 'http://%s:9990/dcs/rest/schematic/instances' % fusion_ip
        return self.dcs_fusion_client.get(uri)

    def dcs_api_get_schematic(self, fusion_ip):
        """
        Return the Schematic details of the DCS.
        | ${resource} | DCS Api Get Schematic  | <fusion_ip> |
        """
        uri = 'http://%s:9990/dcs/rest/schematic/details' % fusion_ip
        return self.dcs_fusion_client.get(uri)

    def dcs_api_get_enc1(self, fusion_ip):
        """
        Return the instances of the enc1.
        | ${resource} | DCS Api Get Enc1  | <fusion_ip> |
        """
        uri = 'http://%s:9990/dcs/rest/schematic/instances/TbChassisModel-1' % fusion_ip
        return self.dcs_fusion_client.get(uri)

    def dcs_api_get_blade(self, fusion_ip, blade_id):
        """
        Return the bladeId(RedBird-20459) of the DCS.
        | ${resource} | DCS Api Get Blade  | <fusion_ip> | <blade_id> |
        """
        uri = 'http://%s:9990/dcs/rest/schematic/instances/%s' % (fusion_ip, blade_id)
        return self.dcs_fusion_client.get(uri)

    def dcs_api_post_blade_power(self, fusion_ip, blade_id):
        """
        toggle the power of blade(Condor-4790).
        | ${resource} | DCS Api Post Blade Power  | <fusion_ip> |
        """
        uri = 'http://%s:9990/dcs/rest/schematic/instances/%s?action=presspowerbutton' % (fusion_ip, blade_id)
        return self.dcs_fusion_client.post(uri)

    def dcs_api_post_blade_set_dimmmemoryfault(self, fusion_ip, blade_id, proc, dimm):
        """
        set blade(condor-4790) dimm memory fault.
        | ${resource} | DCS Api Post Blade Set DimmMemoryFault  | <fusion_ip> | | <proc> | | <dimm> |
        """
        uri = 'http://%s:9990/dcs/rest/schematic/instances/%s?action=setdimmmemoryfault&processorNumber=%s&dimmNumber=%s' % (fusion_ip, blade_id, proc, dimm)
        return self.dcs_fusion_client.post(uri)

    def dcs_api_post_blade_clear_dimmmemoryfault(self, fusion_ip, blade_id, proc, dimm):
        """
        blade clear dimm memory fault.
        | ${resource} | DCS Api Post Blade Clear DimmMemoryFault  | <fusion_ip> |
        """
        uri = 'http://%s:9990/dcs/rest/schematic/instances/%s?action=cleardimmmemoryfault&processorNumber=%s&dimmNumber=%s' % (fusion_ip, blade_id, proc, dimm)
        return self.dcs_fusion_client.post(uri)

    def dcs_api_post_get_server_memory(self, fusion_ip, body, headers=None):
        """
        Get the server memory - processor, DIMM and AMP details.
        | ${resource} | DCS Api Post Get Server Memory  | <fusion_ip> |
        """

        uri = 'http://%s:9990/dcs/rest/passThrough/' % fusion_ip
        response = self.dcs_fusion_client.post(uri=uri, headers=headers, body=json.dumps(body))
        return response

    def dcs_api_post_get_server_dimm(self, fusion_ip, body):
        """
        Get the server memory dimm - DIMM.
        | ${resource} | DCS Api Post Get Server Dimm  | <fusion_ip> |
        """

        uri = 'http://%s:9990/dcs/rest/passThrough/' % fusion_ip
        response = self.dcs_fusion_client.post(uri=uri, body=json.dumps(body))
        return response

    def dcs_api_post_blade_remove_dimm(self, fusion_ip, blade_id, proc, dimm):
        """
        Blade(condor-4790)  Remove Dimm.
        | ${resource} | DCS Api Post Blade Remove Dimm  | <fusion_ip> |
        """
        uri = 'http://%s:9990/dcs/rest/schematic/instances/%s?action=removedimmmemory&processorNumber=%s&dimmNumber=%s' % (fusion_ip, blade_id, proc, dimm)
        return self.dcs_fusion_client.post(uri)

    def dcs_api_post_remove_blade(self, fusion_ip, enc_id, blade_slot):
        """
        Remove blade at given blade location in given enclosure (TbChassisModel-1).
        | ${resource} | DCS Api Post Remove Blade  | <fusion_ip> | |<enc id> ||<blade number> |
        """
        uri = 'http://%s:9990/dcs/rest/schematic/instances/%s?action=removeblade&bayNum=%s' % (fusion_ip, enc_id, blade_slot)
        return self.dcs_fusion_client.post(uri)

    def dcs_api_post_add_blade(self, fusion_ip, enc_id, blade_id, blade):
        """
        Add blade (4591) at given location in given enclosure.
        | ${resource} | DCS Api Post Add Blade | <fusion_ip> | |<enc id> | |<blade id> | | <blade number> |
        """
        uri = 'http://%s:9990/dcs/rest/schematic/instances/%s?action=addblade&bladeId=%s&bayNum=%s' % (fusion_ip, enc_id, blade_id, blade)
        return self.dcs_fusion_client.post(uri)

    def dcs_api_post_remove_interconnect(self, fusion_ip, enc_id, bay):
        """
        Remove interconnect at given bay location in given enclosure (TbChassisModel-1).
        | ${resource} | DCS Api Post Remove Interconnect  | <fusion_ip> | |<enc id> ||<bay number> |
        """
        uri = 'http://%s:9990/dcs/rest/schematic/instances/%s?action=removeinterconnect&bayNum=%s' % (fusion_ip, enc_id, bay)
        return self.dcs_fusion_client.post(uri)

    def dcs_api_post_add_interconnect(self, fusion_ip, enc_id, ic_bay, bay):
        """
        Add interconnect (4591) at given location in given enclosure.
        | ${resource} | DCS Api Post Add Interconnect | <fusion_ip> | |<enc id> | |<ic> | | <bay> |
        """
        uri = 'http://%s:9990/dcs/rest/schematic/instances/%s?action=addinterconnect&bladeId=%s&bayNum=%s' % (fusion_ip, enc_id, ic_bay, bay)
        return self.dcs_fusion_client.post(uri)
