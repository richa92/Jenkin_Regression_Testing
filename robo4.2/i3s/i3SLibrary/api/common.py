#!/usr/bin/python
from RoboGalaxyLibrary.api.common import HTTPClient
from RoboGalaxyLibrary.utilitylib import logging as logger
uris = {
    'loginSessions': "/rest/login-sessions",
    'goldenimage': "/rest/golden-images",
    'goldenvolume': "/rest/goldenvolume",
    'buildplan': "/rest/build-plans",
    'planscript': "/rest/plan-scripts",
    'oedeploymentplan': "/rest/deployment-plans",
    'artifactbundle': "/rest/artifact-bundles",
    'statelessserver': "/rest/statelessserver",
    'auditlog': "/rest/audit-logs",
    'supportdump': "/rest/appliance/support-dumps",
    'deploymentgrp': "/rest/deployment-groups",
    'backup': "/rest/artifact-bundles/backups/archive",
    'osvolumes': '/rest/os-volumes'
}

goldenimageuploadfile = {
    'valid_file_nt': "c:/Goldenimage/ESXi-6.5.0-U1-2017-08-03.zip",
    'invalid_file_nt': "c:/Goldenimage/xyz.txt",
    'valid_file_linux': "/root/Goldenimage/ESXi-6.5.0-U1-2017-08-03.zip",
    'invalid_file_linux': "/root/Goldenimage/xyz.txt"
}

artifactbundleuploadfile = {
    'esx_6.X': "c:/Goldenimage/4.1/HPE-ESX-4.1.zip",
    'rhel7.X': "c:/Goldenimage/4.1/RHEL-7.X-4.1.zip",
    'sles12.1': "c:/Goldenimage/4.1/SLES-12-4.1.zip"
}
goldenimagedownloadfile = {
    'gi_valid_download_file': "c:/GoldenImage_download/esxi6.zip",	
    'gi_invalid_download_file': "c:/GoldenImage_download/xyz.txt",
}
artifactbundle = {
    'ab_downloadtolocation': "c:/Goldenimage/ab_download.zip",
    'ab_uploadfromlocation': "c:/Goldenimage/HPE-ESXi-2017-10-09-v4.0.zip"
}
supportdump = {
    'sd_win_downloadtolocation': "c:/Goldenimage/sd_download.sdmp",
    'sd_linux_downloadtolocation': "/root/sd_download.sdmp"
}
auditlog = {
    'al_win_downloadtolocation': "c:/Goldenimage/al_download.zip",
    'al_linux_downloadtolocation': "/root/al_download.zip"
}
backup = {
    'bk_downloadtolocation': "c:/Goldenimage/backup_download.zip"
}


class i3SAPIBase(object):

    def __init__(self, protocol="https"):
        self._default_headers = {
            'Accept': 'application/json',
            'content-type': 'application/json'}

        self._i3S_protocol_base = protocol + "://"

    def get_headers(self):
        return self._default_headers

    def get_base_url(self):
        return self._i3S_protocol_base


class Authenticate(object):

    def __init__(self):
        self._http = HTTPClient.HTTPClient()
        self.i3S_base = i3SAPIBase()
        self._headers = self.i3S_base.get_headers()

    def login(self, ip, username, passwrd, domain="LOCAL"):
        self._domain = domain
        self._username = username
        self._passwrd = passwrd

        i3S_base = i3SAPIBase()
        headers = i3S_base.get_headers()
        base_url = i3S_base._i3S_protocol_base + ip

        uri = '%s%s' % (base_url, uris.get('loginSessions'))

        data = {
            "userName": self._username,
            "password": self._passwrd}
        response = self._http.post(uri, data, headers)

        return response.status, response.body


def ValueEquals(dictionary1, dictionary2):
    compareOutput = True
    for key1 in dictionary1:
        for key2 in dictionary2:
            if key1 == key2:
                if (key1 == key2 == 'date'):
                    continue
                elif dictionary1[key1] != dictionary2[key2]:
                    compareOutput = False
                    break
    return compareOutput
