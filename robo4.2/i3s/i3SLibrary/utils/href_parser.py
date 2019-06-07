#!/usr/bin/env python
# Copyright 2018 Hewlett Packard Enterprise Development Company LP
#
"""
Interface class to HTML Parser that helps in extracting the latest build
information from HPE Fusion repositories. The fusion repositories include
- Fusion
- ImageStreamer
- OneView Deployment Manager
- DCS

Based on the configured file extension the latest version is returned
"""
import re
from HTMLParser import HTMLParser
from RoboGalaxyLibrary.utilitylib import logging as log


class HRefParser(HTMLParser):
    """
    Helper class to retrieve the latest version
    """
    def __init__(self, file_type='ova'):
        HTMLParser.__init__(self)
        self.file_type = file_type
        self.links = []
        self.link_flag = False

    def handle_starttag(self, tag, attrs):
        """
        Set the Link Flag to True when it sees 'A' element
        :param tag:
        :param attrs:
        :return:
        """
        self.link_flag = True if tag == 'a' else False

    def handle_endtag(self, tag):
        """
        Set the Link Flag to False when it parses '/A' element
        :param tag:
        :return:
        """
        self.link_flag = False if tag == 'a' else self.link_flag

    def handle_data(self, data):
        """
        If it is an 'a href' element and matches the configured file extension,
        add the link to the list
        :param data:
        :return:
        """
        if self.link_flag and data.endswith(self.file_type):
            self.links.append(data)

    def get_latest_build_url(self, pass_build=False):
        """
        Returns the latest build version parsed from the web-page
        :param pass_build: Boolean - True if latest qualified build is required
        :return: (String) URL of the latest version
        """
        versions = []

        for item in self.links:
            # Assumption version of build follows the below format
            # HPEOneView-SSH-4.00.00-0320050_signed-withsig_PASS112.zip
            if pass_build:
                if 'PASS' not in item:
                    continue

            version = re.findall("\d{6}", item)
            if version:
                versions.append(version[0])

        m = "INFO: Available builds in the web-page: {}".format(versions)
        log._log_to_console_and_log_file(m)
        versions.sort()

        latest_version = versions[-1] if len(versions) else None

        for i in self.links:
            if latest_version in i:
                return i

        return None

    def get_build_links(self):
        """
        Returns the list of all available builds
        :return: (List)
        """
        m = "INFO: Builds in the web-page: {}".format(self.links)
        log._log_to_console_and_log_file(m)

        return self.links
