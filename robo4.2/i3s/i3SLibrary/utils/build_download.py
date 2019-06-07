#!/usr/bin/env python
# Copyright 2018 Hewlett Packard Enterprise Development Company LP
#
"""
Helper class for download the OneView Deployment Manager binaries from the
fusion repository
"""
import urllib3
import platform
import os.path
import subprocess
import shlex
import hashlib
from robot.api.deco import keyword
from href_parser import HRefParser
from distutils.spawn import find_executable
from RoboGalaxyLibrary.utilitylib import logging as log


class BuildDownload(object):
    def __init__(self):
        """
        Initializes the helper class
        """
        self.http = urllib3.PoolManager()
        self.webpage = None
        self.url = None
        self.dest = None
        self.proxy = None
        self.file_type = 'ova'
        self.c_sum = None

    def _set_proxy(self):
        """
        Sets the proxy required for downloading the interface

        :return:
        """
        self.http = urllib3.ProxyManager(self.proxy)
        m = "INFO: Proxy is configured to {}".format(self.proxy)
        log._log_to_console_and_log_file(m)

    def _set_build_link(self, pass_build=False):
        """
        Sets the URL to the link of the latest build
        :param pass_build: (Optional) Downloads the latest build marked PASS
        :return:
        """
        r = self.http.request('GET', self.webpage)
        page_parser = HRefParser(self.file_type)
        page_parser.feed(r.data)
        self.url = self.webpage + page_parser.get_latest_build_url(pass_build)
        m = "INFO: The latest build link is {}".format(self.url)
        log._log_to_console_and_log_file(m)

    def _list_builds_of_type(self, f_type):
        """
        Returns a list of builds
        :param f_type: File extension
        :return: (List) Links containing download information
        """
        r = self.http.request('GET', self.webpage)
        pp = HRefParser(self.file_type)
        pp.feed(r.data)
        return [self.webpage + l for l in pp.get_build_links()]

    def _set_checksum(self):
        """
        Retrieve and set the checksum variable. The method assumes that all
        OneView artifacts checksums is stored in .sha256 file.
        :return:
        """
        _link = self.url + '.sha256'
        r = self.http.request('GET', _link)
        if r.status == 200:
            self.c_sum = r.data.split()[0]
            m = "INFO: Checksum information {}".format(r.data)
            log._log_to_console_and_log_file(m)
        else:
            m = "WARN: Checksum information unavailable"
            log._log_to_console(m)

    def _download(self):
        """
        Downloads the build using urllib3
        :return: Name of the file downloaded or None
        """
        f_name = self.url.split('/')[-1]
        f_name = os.path.join(self.dest, f_name)
        resp = self.http.request('GET', self.url, preload_content=False)
        cs = hashlib.sha256()
        with open(f_name, 'wb') as fh:
            for c in resp.stream():
                if c:
                    fh.write(c)
                    cs.update(c)

        resp.release_conn()
        cs = cs.hexdigest()
        m = "INFO: Checksum of {} is {}".format(f_name, cs)
        log._log_to_console_and_log_file(m)

        # Verify the download
        if self.c_sum:
            if cs == self.c_sum:
                m = "INFO: File download completed successfully."
                log._log_to_console_and_log_file(m)
                return self.url.split('/')[-1]
            else:
                m = "Error: Something went wrong. Invalid checksum"
                log._log_to_console_and_log_file(m)
                return None

        return self.url.split('/')[-1]

    def _download_with_accelerator(self):
        """
        Download file using aria2c cli using subprocess module
        :return: Name of the file downloaded or None
        """
        cmd = 'aria2c' if platform.system() is 'Linux' else 'aria2c.exe'
        cmd += ' -x 16 -s 16 '
        cmd += '-d %s ' % self.dest

        if self.proxy:
            cmd += '--all-proxy=%s ' % self.proxy

        if self.c_sum:
            cmd += '--checksum=sha-256=%s ' % self.c_sum

        cmd += self.url
        cmd = shlex.split(cmd)
        proc = subprocess.Popen(cmd, stderr=subprocess.PIPE,
                                stdout=subprocess.PIPE)
        out, err = proc.communicate()

        if proc.returncode == 0 :
            m = "INFO: Download successful.\n%s\nOutput\n%s" % (cmd, out)
            log._log_to_console_and_log_file(m)
            return self.url.split('/')[-1]
        else:
            m = "Error: Something went wrong. \n%s\n%s" % (out, err)
            log._log_to_console_and_log_file(m)
            return None

    def _trigger_download(self, **kwargs):
        """
        Prepare the environment for download and begin the file download
        :param kwargs: Key/value pairs, the below are supported
                       URL - File to download or webpage to get the build
                       dest - Download location for the file.
                       proxy - Proxy information <proto>://<ip>:<port>/
                       latest - boolean True|False to download latest build
                       f_type - Type of file to be downloaded OVA|ZIP|ISO
                       list_flag - boolean True|False to download all builds
        :return: Name of the file downloaded or None
        """
        _url = kwargs['url']
        self.dest = kwargs['dest']
        self.proxy = kwargs['proxy'] if 'proxy' in kwargs else None
        self.file_type = kwargs['f_type'] if 'f_type' in kwargs else 'ova'
        l_flag = kwargs['latest'] if 'latest' in kwargs else False
        p_flag = kwargs['pass_build'] if 'pass_build' in kwargs else False
        list_flag = kwargs['list_flag'] if 'list_flag' in kwargs else False

        if self.proxy:
            self._set_proxy()

        if l_flag:
            self.webpage = _url
            self._set_build_link(p_flag)
        else:
            self.url = _url

        self._set_checksum()
        # Check if aria2c executable is available
        exec_file  = 'aria2c' if platform.system() is 'Linux' else 'aria2c.exe'
        acc_flag = find_executable(exec_file)

        if list_flag:
            self.webpage = _url
            status = []
            for i in self._list_builds_of_type(self.file_type):
                self.url = i
                if acc_flag:
                    s = self._download_with_accelerator()
                else:
                    s = self._download()

                if s:
                    m = "INFO: Download of {} is successful".format(i)
                else:
                    m = "ERROR: Download of {} is unsuccessful".format(i)

                log._log_to_console_and_log_file(m)
                status.append(s)

            return status
        else:
            if acc_flag:
                return self._download_with_accelerator()
            else:
                return self._download()

    ###############################################################
    # Custom Robot Framework keywords for downloading OV artifacts
    ###############################################################
    @keyword(name="Download OVA Build")
    def download_latest_appliance(self, url, dest, proxy=None):
        """
        Downloads the latest OVA from the given website

        Usage:
          Download OVA Build    | <url> | <dest> | <proxy>

        :param url: URL of the web-page to retrieve the latest build link
        :param dest: Folder to download the appliance
        :param proxy: (Optional) PROXY URL
        :return: Name of the file downloaded or None
        """
        return self._trigger_download(url=url, dest=dest, proxy=proxy,
                                      f_type='ova', latest=True)

    @keyword(name="Download OVA Pass Build")
    def download_last_pass_appliance(self, url, dest, proxy=None):
        """
        Downloads the latest Pass build of the appliance from the provided
        website

        Usage
          Download OVA Pass Build    | <url> | <dest> | <proxy>

        :param url: URL of the web-page to retrieve the latest Pass build link
        :param dest: Folder to download the appliance
        :param proxy: (Optional) Proxy URL
        :return: Name of the file downloaded or None
        """
        return self._trigger_download(url=url, dest=dest, proxy=proxy,
                                      f_type='ova', latest=True,
                                      pass_build=True)

    @keyword(name="Download ZIP Build")
    def download_latest_zip(self, url, dest, proxy=None):
        """
        Downloads the latest OVA from the given website

        Usage
          Download ZIP Build    | <url> | <dest> | <proxy>

        :param url: URL of the web-page to retrieve the latest build link
        :param dest: Folder to download the appliance
        :param proxy: (Optional) PROXY URL
        :return: Name of the file downloaded or None
        """
        return self._trigger_download(url=url, dest=dest, proxy=proxy,
                                      f_type='zip', latest=True)

    @keyword(name="Download ZIP Pass Build")
    def download_last_pass_ov(self, url, dest, proxy=None):
        """
        Downloads the latest Pass build of OneView from the website

        Usage
          Download ZIP Pass Build  | <url> | <dest> | <proxy>

        :param url: URL of the web-page to retrieve the latest pass build
        :param dest: Folder to download the appliance
        :param proxy: (Optional) Proxy URL
        :return: Name of the file downloaded or None
        """
        return self._trigger_download(url=url, dest=dest, proxy=proxy,
                                      f_type='zip', latest=True,
                                      pass_build=True)

    @keyword(name="Download Latest File By Type")
    def download_file_by_type(self, url, dest, f_type, proxy=None):
        """
        Downloads the latest build from the web-page based on file type

        Usage
          Download Latest File By Type  | <url> | <dest> | <f_type> | <proxy>

        :param url: URL of the web-page to retrieve the latest build
        :param dest: Folder to download the file
        :param f_type: File extension
        :param proxy: (Optional) Proxy URL
        :return: Name of the file downloaded or None
        """
        return self._trigger_download(url=url, dest=dest, f_type=f_type,
                                      latest=True, proxy=proxy)

    @keyword(name="Download File")
    def download_file(self, url, dest, proxy=None):
        """
        Downloads the file found in the URL

        Usage
          Download File    | <url | <destn> | <proxy>

        :param url: ULR of the binary
        :param dest:  Folder to download the file
        :param proxy: (Optional) Proxy URL
        :return: Name of the file downloaded or None
        """
        return self._trigger_download(url=url, dest=dest, proxy=proxy)

    @keyword(name="Download All Files of Type")
    def download_all_files(self, url, dest, f_type, proxy=None):
        """
        Downloads all the files in the web page
        :param url: URL of the web-page to download the builds
        :param dest: Folder to download the file
        :param f_type: File extension
        :param proxy: (Optional) Proxy URL
        :return: List of filenames or None for failure ones
        """
        return self._trigger_download(url=url, dest=dest, f_type=f_type,
                                      proxy=proxy, list_flag=True)
