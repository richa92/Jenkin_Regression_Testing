from robot.libraries.BuiltIn import BuiltIn
from RoboGalaxyLibrary.utilitylib import logging as logger
import subprocess
import json
import re

fusion_lib = BuiltIn().get_library_instance('FusionLibrary')


def lookup_server_profile_template_volume_attachment_ATAI(spt):
    """
    :param: spt: volume attachment ATAI will be looked up from the SPT DTO if "SPTVAID:<id>" is defined.
            spt_edit = {
                "type":"ServerProfileTemplateV400","name":SPT1_NAME,
                "serverHardwareTypeUri":'SHT:'+SHT1,"enclosureGroupUri":'EG:'+EG_NAME,
                "iscsiInitiatorNameType":"UserDefined",
                "serialNumberType":"Virtual","macType":"Virtual","wwnType":"Virtual","affinity":"Bay",
                "connections":[
                     {"id":1,"name":"","functionType":"FibreChannel","portId":"Mezz 2:1","requestedMbps":"Auto","networkUri":'FC:fa-a',},
                     {"id":2,"name":"","functionType":"FibreChannel","portId":"Mezz 2:2","requestedMbps":"Auto","networkUri":'FC:fa-b',},
                     {"id":3,"name":"","functionType":"iSCSI","portId":"Flb 1:1-b","requestedMbps":"2500","networkUri":"ETH:network-untagged","ipv4":{}},
                     {"id":4,"name":"","functionType":"iSCSI","portId":"Flb 1:2-b","requestedMbps":"2500","networkUri":"ETH:network-untagged","ipv4":{}},
                     {"id":5,"name":"","functionType":"Ethernet","portId":"Mezz 1:1-a","requestedMbps":"2500","networkUri":"ETH:network-tunnel","ipv4":{}},
                     {"id":6,"name":"","functionType":"Ethernet","portId":"Mezz 1:2-a","requestedMbps":"2500","networkUri":"ETH:network-tunnel","ipv4":{}}
                 ],
                "boot":{"manageBoot":True,"order":["HardDisk","CD","Floppy","USB","PXE"]},"bootMode":None,
                "firmware":{"manageFirmware":False,"firmwareBaselineUri":"","forceInstallFirmware":False,"firmwareInstallType":None},
                "bios":{"manageBios":False,"overriddenSettings":[]},
                "localStorage":{"sasLogicalJBODs":[],"controllers":[]},
                "sanStorage":{"hostOSType":"VMware (ESXi)","manageSanStorage":True,
                    "volumeAttachments":[
                        {"id":1,"volumeUri":"SVOL:"+VOLUME_SHARED_3PAR1,"isBootVolume":False,"lunType":"Manual","lun":None,
                        "associatedTemplateAttachmentId":'SPTVAID:1',
                         "storagePaths":[{"isEnabled":True,"connectionId":1,"targetSelector":"Auto","targets":[]},
                                         {"isEnabled":True,"connectionId":2,"targetSelector":"Auto","targets":[]}]
                         },
                        {"id":2,"volumeUri":"SVOL:"+VOLUME_SHARED_VSA2,"isBootVolume":False,"lunType":"Auto","lun":None,
                        "associatedTemplateAttachmentId":'SPTVAID:2',
                         "storagePaths":[{"isEnabled":False,"connectionId":5,"targetSelector":"Auto","targets":[]},
                                         {"isEnabled":False,"connectionId":6,"targetSelector":"Auto","targets":[]}]
                         },
                    ]
                }
            }
    :return: spt: updated spt with volume attachment ATAI.
    """
    if isinstance(spt, dict) and re.search('ServerProfileTemplate', spt['type']):
        lookup_ATAI = False
        if 'sanStorage' in spt and 'volumeAttachments' in spt['sanStorage'] and len(spt['sanStorage']['volumeAttachments']) != 0:
            for va in spt['sanStorage']['volumeAttachments']:
                if 'associatedTemplateAttachmentId' in va and va['associatedTemplateAttachmentId'] is not None and re.search("^SPTVAID", va['associatedTemplateAttachmentId']):
                    lookup_ATAI = True
        if lookup_ATAI:
            logger._debug('Lookup volume attachment ATAI for SPT %s' % spt['name'])
            param = "?filter='name'='%s'" % spt['name']
            response = fusion_lib.fusion_api_get_server_profile_templates(param=param)
            if response['status_code'] == 200 and response['count'] == 1:
                spt_dto = response['members'][0]
                logger._debug("The SPT DTO is %s" % spt_dto)
                if 'sanStorage' in spt_dto and 'volumeAttachments' in spt_dto['sanStorage'] and len(spt_dto['sanStorage']['volumeAttachments']) != 0:
                    vas = spt['sanStorage']['volumeAttachments']
                    vas_spt = spt_dto['sanStorage']['volumeAttachments']  # volume attachments in the SPT DTO
                    for va in vas:
                        if 'associatedTemplateAttachmentId' in va and va['associatedTemplateAttachmentId'] is not None and re.search("^SPTVAID", va['associatedTemplateAttachmentId']):
                            rtn = re.search("^(SPTVAID):(\d*)$", va['associatedTemplateAttachmentId'])
                            spt_va_id = int(rtn.group(2))
                            logger._debug("SPTVAID is %s" % spt_va_id)
                            found = False
                            for va_spt in vas_spt:
                                if va_spt['id'] == spt_va_id:
                                    found = True
                                    logger._debug("ATAI for template volume id %s is %s" % (spt_va_id, va_spt['associatedTemplateAttachmentId']))
                                    va['associatedTemplateAttachmentId'] = va_spt['associatedTemplateAttachmentId']
                            if not found:
                                va['associatedTemplateAttachmentId'] = None
                    logger._debug("After look up ATAI, SPT is now %s" % spt)
                    return spt
                else:
                    raise AssertionError("No sanStorage or volume attachments defined in SPT DTO")
            else:
                raise AssertionError("SPT DTO not found for %s" % spt['name'])
        else:
            logger._debug('No need to lookup volume attachment ATAI for %s' % spt['name'])
            return spt
    else:
        raise AssertionError("The argument spt %s is not SPT DTO" % spt)


def lookup_server_profile_volume_attachment_ATAI(profile):
    """
    :param: profile: volume attachment ATAI will be looked up from the SPT DTO if "SPTVAID:<id>" is defined.
        profile_edit = {
            "type":"ServerProfileV400","name":SPT1_PROFILE1_NAME,"description":None,
            "serverHardwareUri":'SH:'+ENC1SHBAY1,"enclosureGroupUri":'EG:'+EG_NAME,"enclosureUri":'ENC:'+ENC1,
            "serverProfileTemplateUri":"SPT:"+SPT1_NAME,
            "iscsiInitiatorNameType":"UserDefined","iscsiInitiatorName":SPT1_PROFILE1_IQN,
            "serialNumberType":"Virtual","macType":"Virtual","wwnType":"Virtual","affinity":"Bay",
            "hideUnusedFlexNics":True,"osDeploymentSettings":None,
            "connections":[
                {"id":1,"name":"","functionType":"FibreChannel","portId":"Mezz 2:1","requestedMbps":"Auto","networkUri":'FC:fa-a',},
                {"id":2,"name":"","functionType":"FibreChannel","portId":"Mezz 2:2","requestedMbps":"Auto","networkUri":'FC:fa-b',},
                {"id":3,"name":"","functionType":"iSCSI","portId":"Flb 1:1-b","requestedMbps":"2500","networkUri":"ETH:network-untagged",},
                {"id":4,"name":"","functionType":"iSCSI","portId":"Flb 1:2-b","requestedMbps":"2500","networkUri":"ETH:network-untagged",},
                {"id":5,"name":"","functionType":"Ethernet","portId":"Mezz 1:1-a","requestedMbps":"2500","networkUri":"ETH:network-tunnel"},
                {"id":6,"name":"","functionType":"Ethernet","portId":"Mezz 1:2-a","requestedMbps":"2500","networkUri":"ETH:network-tunnel"}
             ],
            "boot":{"manageBoot":True,"order":["HardDisk","CD","Floppy","USB","PXE"]},"bootMode":None,
            "firmware":{"manageFirmware":False,"firmwareBaselineUri":None,"forceInstallFirmware":False,"firmwareInstallType":None},
            "bios":{"manageBios":False,"overriddenSettings":[]},
            "localStorage":{"sasLogicalJBODs":[],"controllers":[]},
            "sanStorage":{"hostOSType":"RHE Linux (5.x, 6.x)","manageSanStorage":True,
                "volumeAttachments":[
                    {"id":1,"volumeUri":"SVOL:c7000-shared-3par1","isBootVolume":False,"lunType":"Manual","lun":0,
                     "associatedTemplateAttachmentId":'SPTVAID:1',
                     "storagePaths":[
                         {"isEnabled":True,"connectionId":1,"targetSelector":"Auto",},
                         {"isEnabled":False,"connectionId":2,"targetSelector":"Auto",},]
                     },
                ]
            }
        }
    :return: profile: updated profile with volume attachment ATAI.
    """
    if isinstance(profile, dict) and re.search('ServerProfile', profile['type']):
        lookup_ATAI = False
        if 'sanStorage' in profile and 'volumeAttachments' in profile['sanStorage'] and len(profile['sanStorage']['volumeAttachments']) != 0:
            for va in profile['sanStorage']['volumeAttachments']:
                if 'associatedTemplateAttachmentId' in va and va['associatedTemplateAttachmentId'] is not None and re.search("^SPTVAID", va['associatedTemplateAttachmentId']):
                    lookup_ATAI = True
        if lookup_ATAI:
            logger._debug('Lookup volume attachment ATAI for profile %s' % profile['name'])
            param = "?filter='name'='%s'" % profile['name']
            response = fusion_lib.fusion_api_get_server_profiles(param=param)
            if response['status_code'] == 200 and response['count'] == 1:
                profile_dto = response['members'][0]
                logger._debug("The profile DTO is %s" % profile_dto)
                if 'serverProfileTemplateUri' in profile_dto and profile_dto['serverProfileTemplateUri'] is not None:
                    spt_uri = profile_dto['serverProfileTemplateUri']
                    spt_dto = fusion_lib.fusion_api_get_resource(uri=spt_uri)
                    logger._debug("The SPT DTO is %s" % spt_dto)
                    if 'sanStorage' in spt_dto and 'volumeAttachments' in spt_dto['sanStorage'] and len(spt_dto['sanStorage']['volumeAttachments']) != 0:
                        vas = profile['sanStorage']['volumeAttachments']
                        vas_spt = spt_dto['sanStorage']['volumeAttachments']  # volume attachments in the SPT DTO
                        for va in vas:
                            if 'associatedTemplateAttachmentId' in va and va['associatedTemplateAttachmentId'] is not None and re.search("^SPTVAID", va['associatedTemplateAttachmentId']):
                                rtn = re.search("^(SPTVAID):(\d*)$", va['associatedTemplateAttachmentId'])
                                spt_va_id = int(rtn.group(2))
                                for va_spt in vas_spt:
                                    logger._debug("id for va_spt is %s" % va_spt['id'])
                                    if va_spt['id'] == spt_va_id:
                                        logger._debug("ATAI for template volume id %s is %s" % (spt_va_id, va_spt['associatedTemplateAttachmentId']))
                                        va['associatedTemplateAttachmentId'] = va_spt['associatedTemplateAttachmentId']
                        logger._debug("After look up ATAI in SPT, profile is now %s" % profile)
                        return profile
                    else:
                        raise AssertionError("No sanStorage or volume attachments defined in SPT DTO")
                else:
                    raise AssertionError("serverProfileTemplateUri is not defined in profile DTO for profile %s" % profile['name'])
            else:
                raise AssertionError("Profile DTO not found for profile %s" % profile['name'])
        else:
            logger._debug('No need to lookup volume attachment ATAI for profile %s' % profile['name'])
            return profile
    else:
        raise AssertionError("The argument profile %s is not profile DTO" % profile)


def lookup_volume_attachment_atai_for_server_profile_from_template(profile):
    """
    :param: profile: A server profile DTO that contains a serverProfileTemplateUri. The volume attachment ATAI will be looked up from the SPT DTO if "SPTVAID:<id>" is defined.

        profile_dto_example:
        {
            "type":"ServerProfileV8","name":SPT1_PROFILE1_NAME,"description":None,
            "serverHardwareUri":'SH:'+ENC1SHBAY1,"enclosureGroupUri":'EG:'+EG_NAME,"enclosureUri":'ENC:'+ENC1,
            "serverProfileTemplateUri":"SPT:"+SPT1_NAME,
            "iscsiInitiatorNameType":"UserDefined","iscsiInitiatorName":SPT1_PROFILE1_IQN,
            "serialNumberType":"Virtual","macType":"Virtual","wwnType":"Virtual","affinity":"Bay",
            "hideUnusedFlexNics":True,"osDeploymentSettings":None,
            "connections":[
                {"id":1,"name":"","functionType":"FibreChannel","portId":"Mezz 2:1","requestedMbps":"Auto","networkUri":'FC:fa-a',},
                {"id":2,"name":"","functionType":"FibreChannel","portId":"Mezz 2:2","requestedMbps":"Auto","networkUri":'FC:fa-b',},
                {"id":3,"name":"","functionType":"iSCSI","portId":"Flb 1:1-b","requestedMbps":"2500","networkUri":"ETH:network-untagged",},
                {"id":4,"name":"","functionType":"iSCSI","portId":"Flb 1:2-b","requestedMbps":"2500","networkUri":"ETH:network-untagged",},
                {"id":5,"name":"","functionType":"Ethernet","portId":"Mezz 1:1-a","requestedMbps":"2500","networkUri":"ETH:network-tunnel"},
                {"id":6,"name":"","functionType":"Ethernet","portId":"Mezz 1:2-a","requestedMbps":"2500","networkUri":"ETH:network-tunnel"}
             ],
            "boot":{"manageBoot":True,"order":["HardDisk","CD","Floppy","USB","PXE"]},"bootMode":None,
            "firmware":{"manageFirmware":False,"firmwareBaselineUri":None,"forceInstallFirmware":False,"firmwareInstallType":None},
            "bios":{"manageBios":False,"overriddenSettings":[]},
            "localStorage":{"sasLogicalJBODs":[],"controllers":[]},
            "sanStorage":{"hostOSType":"RHE Linux (5.x, 6.x)","manageSanStorage":True,
                "volumeAttachments":[
                    {"id":1,"volumeUri":"SVOL:c7000-shared-3par1","isBootVolume":False,"lunType":"Manual","lun":0,
                     "associatedTemplateAttachmentId":'SPTVAID:1',
                     "storagePaths":[
                         {"isEnabled":True,"connectionId":1,"targetSelector":"Auto",},
                         {"isEnabled":False,"connectionId":2,"targetSelector":"Auto",},]
                     },
                ]
            }
        }

    :return: profile: Updated profile with volume attachment ATAI.
    """
    if isinstance(profile, dict) and re.search('ServerProfile', profile['type']):
        lookup_ATAI = False
        if 'sanStorage' in profile and 'volumeAttachments' in profile['sanStorage'] and len(profile['sanStorage']['volumeAttachments']) != 0:
            for va in profile['sanStorage']['volumeAttachments']:
                if 'associatedTemplateAttachmentId' in va and va['associatedTemplateAttachmentId'] is not None and re.search("^SPTVAID", va['associatedTemplateAttachmentId']):
                    lookup_ATAI = True
        if lookup_ATAI:
            spt_uri = profile['serverProfileTemplateUri']
            spt_name = spt_uri.split(':')
            logger._debug('Lookup volume attachment ATAI for SPT %s' % spt_name[1])
            param = "?filter='name'='%s'" % spt_name[1]
            response = fusion_lib.fusion_api_get_server_profile_templates(param=param)
            if response['status_code'] == 200 and response['count'] == 1:
                spt_dto = response['members'][0]
                logger._debug("The SPT DTO is %s" % spt_dto)
                if 'sanStorage' in spt_dto and 'volumeAttachments' in spt_dto['sanStorage'] and len(spt_dto['sanStorage']['volumeAttachments']) != 0:
                    vas = profile['sanStorage']['volumeAttachments']
                    vas_spt = spt_dto['sanStorage']['volumeAttachments']  # volume attachments in the SPT DTO
                    for va in vas:
                        if 'associatedTemplateAttachmentId' in va and va['associatedTemplateAttachmentId'] is not None and re.search("^SPTVAID", va['associatedTemplateAttachmentId']):
                            rtn = re.search("^(SPTVAID):(\d*)$", va['associatedTemplateAttachmentId'])
                            spt_va_id = int(rtn.group(2))
                            logger._debug("SPTVAID is %s" % spt_va_id)
                            found = False
                            for va_spt in vas_spt:
                                if va_spt['id'] == spt_va_id:
                                    found = True
                                    logger._debug("ATAI for template volume id %s is %s" % (spt_va_id, va_spt['associatedTemplateAttachmentId']))
                                    va['associatedTemplateAttachmentId'] = va_spt['associatedTemplateAttachmentId']
                            if not found:
                                va['associatedTemplateAttachmentId'] = None
                    logger._debug("After look up ATAI, SP is now %s" % profile)
                    return profile
                else:
                    raise AssertionError("No sanStorage or volume attachments defined in SPT DTO")
            else:
                raise AssertionError("SPT DTO not found for %s" % spt_name[1])
        else:
            logger._debug('No need to lookup volume attachment ATAI for %s' % profile['name'])
            return profile
    else:
        raise AssertionError("The argument profile %s is not profile DTO" % profile)


def verify_server_profile_volume_attachments(profile):
    """
    :param profile: profile defined in the data file
    :return: verify status, 'PASS' or 'FAIL'
    """
    if isinstance(profile, dict) and re.search('ServerProfile', profile['type']):
        logger._log_to_console_and_log_file('Verifying volume attachments for profile %s' % profile['name'])
        verify = 'PASS'
        param = "?filter='name'='%s'" % profile['name']
        response = fusion_lib.fusion_api_get_server_profiles(param=param)
        if response['status_code'] == 200 and response['count'] == 1:
            profile_uri = response['members'][0]['uri']
        else:
            raise AssertionError("Profile URI not found for profile %s" % profile['name'])
        if 'sanStorage' in profile and 'volumeAttachments' in profile['sanStorage']:
            volume_attachments = profile['sanStorage']['volumeAttachments']
            if len(volume_attachments) != 0:
                for volume_attachment in volume_attachments:
                    volume_name = volume_attachment['volumeName'] if volume_attachment['volumeUri'] is None else volume_attachment['volumeUri']
                    if re.search(':', volume_name):
                        start = volume_name.index(':')
                        volume_name = volume_name[start + 1:]
                    param = "?query=name eq '%s'" % volume_name
                    response = fusion_lib.fusion_api_get_storage_volumes(param=param)
                    if response['status_code'] == 200 and response['count'] == 1:
                        volume_uri = response['members'][0]['uri']
                    else:
                        raise AssertionError("URI not found for volume %s" % volume_name)
                    param = "?query=storageVolumeUri eq '%s' AND ownerUri eq '%s'" % (volume_uri, profile_uri)
                    response = fusion_lib.fusion_api_get_storage_volume_attachments(param=param)
                    if response['status_code'] == 200 and response['count'] == 1:
                        logger._debug("The volume attachment for volume %s and profile %s is %s" % (volume_name, profile['name'], response['members'][0]))
                    else:
                        logger._debug("The volume attachment for volume %s and profile %s is not found: %s" % (volume_name, profile['name'], response))
                        verify = 'FAIL'
            else:
                raise AssertionError("Zero volume attachments defined in profile %s" % profile['name'])
        else:
            raise AssertionError("No sanStorage or volume attachments defined in profile %s" % profile['name'])

        logger._log_to_console_and_log_file('Verify volume attachments for profile %s %s' % (profile['name'], verify))
        return verify
    else:
        raise AssertionError("The argument profile %s is not profile DTO" % profile)
