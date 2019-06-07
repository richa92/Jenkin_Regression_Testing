"""
SPT common module
"""
import re
from RoboGalaxyLibrary.utilitylib import logging as logger
from FusionLibrary.keywords.fusion_api import FusionAPIKeywords
from robot.libraries.BuiltIn import BuiltIn


class spt_common(object):
    """
    SPT  common module is used to handle SPT / SP payload processing,
     which in turn is used in  robo galaxy keyword in resource.txt
    """
    def __init__(self):
        self.fusionlib = BuiltIn().get_library_instance('FusionLibrary')

    def update_spt_volume(self, update_payload):
        """
        This module is designed to generate required update spt payload after comparing storage part of test data with original spt  get payload.
        this module will return required payload to update SPT
         Usage: update_spt_volume(self, update_payload)
        """
        parameter = '?filter=name=\'%s\''
        for u_payload in update_payload:
            param = parameter % u_payload['name']
            get_data = self.fusionlib.fusion_api_get_server_profile_templates(uri=None, api=None, headers=None, param=param)
            for spt in get_data['members']:
                spt_uri = spt['uri']
                spt_etag = spt['eTag']
                get_uri_payload = self.fusionlib.fusion_api_get_server_profile_templates(uri=spt_uri, api=None, headers=None)
                u_storage = []
                for u_vol in u_payload['sanStorage']['volumeAttachments']:
                    vol = {}
                    if 'volumeUri' in u_vol:
                        for org_vol in get_uri_payload['sanStorage']['volumeAttachments']:
                            if org_vol['volumeUri'] is not None:
                                if u_vol['volumeUri'] == org_vol['volumeUri']:
                                    vol = org_vol
                        if not vol:
                            vol = u_vol
                    else:
                        if 'volume' in u_vol:
                            for org_vol in get_uri_payload['sanStorage']['volumeAttachments']:
                                if org_vol['volume'] is not None:
                                    if u_vol['volume']['properties']['name'] == org_vol['volume']['properties']['name']:
                                        vol = org_vol
                            if not vol:
                                vol = u_vol
                    if vol:
                        u_storage.append(vol)
                u_payload['sanStorage']['volumeAttachments'] = u_storage
                u_payload['uri'] = spt_uri
                u_payload['eTag'] = spt_etag
        logger._log_to_console_and_log_file("Generate SPT payload after updating volume %s" % update_payload)
        return update_payload

    def update_sp_volume(self, update_payload):
        """
        This module is designed to generate required update sp payload after comparing storage part of test data with original spt  get payload.
        this module will return required payload to update SPT
         Usage: update_spt_volume(self, update_payload)
        """
        parameter = '?filter=name=\'%s\''
        for u_payload in update_payload:
            param = parameter % u_payload['name']
            get_data = self.fusionlib.fusion_api_get_server_profiles(uri=None, api=None, headers=None, param=param)
            for sp_data in get_data['members']:
                sp_uri = sp_data['uri']
                sp_etag = sp_data['eTag']
                spt = sp_data['serverProfileTemplateUri']
                get_uri_payload = self.fusionlib.fusion_api_get_server_profile_templates(uri=sp_uri, api=None, headers=None)
                u_storage = []
                for u_vol in u_payload['sanStorage']['volumeAttachments']:
                    vol = {}
                    if 'volumeUri' in u_vol:
                        for org_vol in get_uri_payload['sanStorage']['volumeAttachments']:
                            if org_vol['volumeUri'] is not None:
                                if u_vol['volumeUri'] == org_vol['volumeUri']:
                                    vol = org_vol
                        if not vol:
                            vol = u_vol
                    else:
                        if 'volume' in u_vol:
                            for org_vol in get_uri_payload['sanStorage']['volumeAttachments']:
                                if org_vol['volume'] is not None:
                                    if u_vol['volume']['properties']['name'] == org_vol['volume']['properties']['name']:
                                        vol = org_vol
                            if not vol:
                                vol = self.add_template_attachment_id_from_spt(u_vol, spt)
                    if vol:
                        u_storage.append(vol)
                u_payload['sanStorage']['volumeAttachments'] = u_storage
                u_payload['uri'] = sp_uri
                u_payload['eTag'] = sp_etag
        logger._log_to_console_and_log_file("Generate SP payload after updating volume %s" % update_payload)
        return update_payload

    def add_template_attachment_id_from_spt(self, priv_vol, spt_uri):
        """
        In SP private volume payload add volume template attachment id from SPT
        """
        get_spt_data = self.fusionlib.fusion_api_get_server_profile_templates(uri=spt_uri, api=None, headers=None, param='')
        for vol in get_spt_data['sanStorage']['volumeAttachments']:
            if vol['volumeUri'] is None:
                if vol['volume']['properties']['name'] == priv_vol['volume']['properties']['name']:
                    a_id = vol['associatedTemplateAttachmentId']
                    priv_vol['associatedTemplateAttachmentId'] = a_id
                    logger._log_to_console_and_log_file("priv vol %s" % priv_vol)
                    return priv_vol
        return priv_vol

    def remove_sp_spt(self, *payloads):
        parameter = '?filter=name=\'%s\''
        out_resp = []
        sp_uris = []
        spt_uris = []
        for payload in payloads:
            if payload:
                for payload1 in payload:
                    if 'type' in payload1:
                        if re.match("^ServerProfileV", payload1['type']):
                            param = parameter % payload1['name']
                            get_resp = self.fusionlib.fusion_api_get_server_profiles(uri=None, api=None, headers=None, param=param)
                            if 'count' in get_resp:
                                if get_resp['count'] > 0:
                                    if 'members' in get_resp:
                                        sp_uri = get_resp['members'][0]['uri']
                                        if sp_uri not in sp_uris:
                                            sp_uris.append(sp_uri)
                        elif re.match("^ServerProfileTemplateV", payload1['type']):
                            if 'name' in payload1:
                                if payload1['name'] is not None:
                                    if 'new_name' in payload1:
                                        param = parameter % payload1['new_name']
                                    else:
                                        param = parameter % payload1['name']
                                    get_resp1 = self.fusionlib.fusion_api_get_server_profile_templates(uri=None, api=None, headers=None, param=param)
                                    if 'count' in get_resp1:
                                        if get_resp1['count'] > 0:
                                            if 'members' in get_resp1:
                                                spt_uri = get_resp1['members'][0]['uri']
                                                if spt_uri not in spt_uris:
                                                    spt_uris.append(spt_uri)
                    else:
                        if 'SP' in payload1:
                            if 'name' in payload1:
                                if payload1['name'] is not None:
                                    if 'new_name' in payload1:
                                        param = parameter % payload1['new_name']
                                    else:
                                        param = parameter % payload1['name']
                                    get_resp1 = self.fusionlib.fusion_api_get_server_profile_templates(uri=None, api=None, headers=None, param=param)
                                    if 'count' in get_resp1:
                                        if get_resp1['count'] > 0:
                                            if 'members' in get_resp1:
                                                spt_uri = get_resp1['members'][0]['uri']
                                                if spt_uri not in spt_uris:
                                                    spt_uris.append(spt_uri)
        for sp in sp_uris:
            resp = self.fusionlib.fusion_api_delete_server_profile(uri=sp)
            logger._log_to_console_and_log_file("delete sp resp: %s" % resp)
            task_resp = self.fusionlib.fusion_api_wait_for_task_to_complete(resp['headers']['Location'], retries=50)
            logger._log_to_console_and_log_file("delete sp task resp: %s" % task_resp)
        for spt in spt_uris:
            resp = self.fusionlib.fusion_api_delete_server_profile_template(uri=spt)
            logger._log_to_console_and_log_file("delete spt resp: %s" % resp)
            task_resp = self.fusionlib.fusion_api_wait_for_task_to_complete(resp['headers']['Location'])
            logger._log_to_console_and_log_file("delete spt task resp: %s" % task_resp)
