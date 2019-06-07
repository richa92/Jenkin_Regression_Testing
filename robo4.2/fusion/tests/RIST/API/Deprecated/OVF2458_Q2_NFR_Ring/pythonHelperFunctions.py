from robot.libraries.BuiltIn import BuiltIn
from RoboGalaxyLibrary.utilitylib import logging as logger
from copy import deepcopy


#  Vol_Attach_Helper()
#  This is used to obtain actual uri for SSYS:, SPOOL: and SVOL: withing volumeAttachments
#
#  These used to help create "expected" data for Fusion Api Validate Response Follow used by test file 09'
#  SanStorage_Validate_Helper()
#  Expected_Local_Storage()
#  Expected_Connections()
1
fusion_lib = BuiltIn().get_library_instance('FusionLibrary')

logger._log_to_console_and_log_file("")
# expected_error_message = BuiltIn().run_keyword("Get Expected Error", errorMessage, kwargs)
# response = fusion_lib.fusion_api_get_task(uri=uri, param='?view=tree')
wordy = False
reallywordy = False


def Vol_Attach_Helper(profile_sanStorage):

    wasList = True
    if isinstance(profile_sanStorage, dict):
        if wordy:
            logger._log_to_console_and_log_file(
                "profile_sanStorage is a dict.  Convert to list of this task.")
        profile_sanStorage = [profile_sanStorage]
        wasList = False

    uriCache = {}

    for profile in profile_sanStorage:
        if reallywordy:
            logger._log_to_console_and_log_file("Profile: %s" % profile)

        these_volumeAttachment = []
        for volumeAttachment in profile['sanStorage']['volumeAttachments']:

            new_volumeAttachment = deepcopy(volumeAttachment)
            if reallywordy:
                logger._log_to_console_and_log_file(volumeAttachment)

            if "volumeUri" in volumeAttachment and volumeAttachment[
                    'volumeUri'] is not None:
                if volumeAttachment['volumeUri'] in uriCache:
                    volumeUri = uriCache[volumeAttachment['volumeUri']]
                else:
                    volumeUri = BuiltIn().run_keyword(
                        "Common URI lookup by name",
                        volumeAttachment['volumeUri'])
                    uriCache[volumeAttachment['volumeUri']] = volumeUri
                if reallywordy:
                    logger._log_to_console_and_log_file(
                        "volume uri: %s" %
                        volumeUri)
                new_volumeAttachment['volumeUri'] = volumeUri

            if "volumeStoragePoolUri" in volumeAttachment and volumeAttachment[
                    'volumeStoragePoolUri'] is not None:
                if volumeAttachment['volumeStoragePoolUri'] in uriCache:
                    volumeStoragePoolUri = uriCache[
                        volumeAttachment['volumeStoragePoolUri']]
                else:
                    volumeStoragePoolUri = BuiltIn().run_keyword(
                        "Common URI lookup by name",
                        volumeAttachment['volumeStoragePoolUri'])
                    uriCache[
                        volumeAttachment['volumeStoragePoolUri']] = volumeStoragePoolUri
                if reallywordy:
                    logger._log_to_console_and_log_file(
                        "pool uri: %s" %
                        volumeStoragePoolUri)
                new_volumeAttachment[
                    'volumeStoragePoolUri'] = volumeStoragePoolUri

            if "volumeStorageSystemUri" in volumeAttachment and volumeAttachment[
                    'volumeStorageSystemUri'] is not None:
                if volumeAttachment['volumeStorageSystemUri'] in uriCache:
                    volumeStorageSystemUri = uriCache[
                        volumeAttachment['volumeStorageSystemUri']]
                else:
                    volumeStorageSystemUri = BuiltIn().run_keyword(
                        "Common URI lookup by name",
                        volumeAttachment['volumeStorageSystemUri'])
                    uriCache[
                        volumeAttachment['volumeStorageSystemUri']] = volumeStorageSystemUri
                if reallywordy:
                    logger._log_to_console_and_log_file(
                        "system uri: %s" %
                        volumeStorageSystemUri)
                new_volumeAttachment[
                    'volumeStorageSystemUri'] = volumeStorageSystemUri

            these_volumeAttachment.append(new_volumeAttachment)

        profile['sanStorage']['volumeAttachments'] = these_volumeAttachment
        if wordy:
            logger._log_to_console_and_log_file(
                "sanStorage %s" %
                profile['sanStorage'])

    if wordy:
        logger._log_to_console_and_log_file(
            "sanStorage %s" %
            profile_sanStorage)

    if wasList:
        return profile_sanStorage
    else:
        return profile_sanStorage[0]


def Create_Expected_SanStorage(sanStorage, regex):
    # used to add a target regexp for validationin Fusion Api Validate Response Follow as we don't specify targets but
    # the profile will actually have targets specified.

    new_targets = [{
        "name": "REGEX:%s" % regex
    },
        {
        "name": "REGEX:%s" % regex
    }]

    logger._log_to_console_and_log_file("march through volumeAttachments")
    for volumeAttachment in sanStorage['volumeAttachments']:
        for storagePath in volumeAttachment['storagePaths']:
            storagePath['targets'] = new_targets

        # these items part of PUT but not returned in GET
        if 'volumeShareable' in volumeAttachment:
            del volumeAttachment['volumeShareable']
        if 'volumeName' in volumeAttachment:
            volumeAttachment['volumeUri'] = 'SVOL:%s' % volumeAttachment['volumeName']
            del volumeAttachment['volumeName']
        if 'volumeProvisionType' in volumeAttachment:
            del volumeAttachment['volumeProvisionType']
        if 'volumeProvisionedCapacityBytes' in volumeAttachment:
            del volumeAttachment['volumeProvisionedCapacityBytes']
        if 'permanent' in volumeAttachment:
            del volumeAttachment['permanent']

        # in case ids change we don't really care id #.  volumneName is more important
        del volumeAttachment['id']

    return sanStorage


def Expected_Local_Storage(name, spts):
    # used to return the local storage based on name from template 480 or 660
    spt = name[-5:]
    localStorage = spts[spt]['localStorage']

    return localStorage


def Expected_Connections(conns):
    # used to return connections with items removed/altered as needed
    for conn in conns:
        del conn['boot']['iscsi']
        del conn['ipv4']

    # return as a dict as that is what will be needed
    return {'connections': conns}


def Expected_SP_From_SPT(spt, version):
    new_spt = deepcopy(spt)

    if version == 600:
        new_spt['type'] = "ServerProfileV8"
    elif version == 500:
        new_spt['type'] = "ServerProfileV7"

    # removed from SPT when a SP
    del new_spt['serverProfileDescription']
    del new_spt['name']
    del new_spt['firmware']

    # these are verified independetly as data file created dynamically.
    del new_spt['connectionSettings']
    del new_spt['localStorage']
    del new_spt['sanStorage']

    if '480' in new_spt['serverHardwareTypeUri']:
        sht = "480"
    else:
        sht = "660"

    new_spt[
        'serverHardwareTypeUri'] = 'SHT:SY %s Gen9:1:Smart Array P542D Controller:2:Synergy 3830C 16G FC HBA:3:Synergy 3820C 10/20Gb CNA' % sht

    # logger._log_to_console_and_log_file(new_spt)

    return new_spt


def Get_Volume_Name_For_Sorted_By_volumeURI(sanStorage):
    for volumeAttachment in sanStorage['volumeAttachments']:
        volume = fusion_lib.fusion_api_get_resource(volumeAttachment['volumeUri'])
        volumeAttachment['volumeUri'] = 'SVOL:%s' % volume['name']

    return sanStorage


def Create_Expected_Volumes(existing, profile_sanStorage):
    for exist in existing:
        del exist['storageSystemUri']
        exist['isPermanent'] = True

    for profile in profile_sanStorage.keys():
        for volumeName in profile_sanStorage[profile]['sanStorage']['volumeAttachments']:
            if 'volumeName' in volumeName:
                existing.append({'deviceVolumeName': volumeName['volumeName'],
                                 'name': volumeName['volumeName'],
                                 'isShareable': False,
                                 'isPermanent': False})
    return {'members': existing}
