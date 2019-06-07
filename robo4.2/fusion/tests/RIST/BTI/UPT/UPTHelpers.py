from enum import Enum
from FusionLibrary.libs.cli.cli_base import local_actions
import os
import re
from RoboGalaxyLibrary.utilitylib import logging as logger
from robot.libraries.BuiltIn import BuiltIn
import requests
import string
import threading
import urllib2
import urllib3
import yaml


def build_updatebin_files(updatebin_urls):
    """
    Build dictionary of updatebin files
    :param updatebin_urls:
    :return updatebin_files:
    """
    updatebin_files = {}
    for k in updatebin_urls.keys():
        url = updatebin_urls[k]
        filename = url.split('/')[-1]
        updatebin_files[k] = filename

    return updatebin_files


def build_updatebin_urls(updatebin_urls_file):
    """
    Build dictionary of updatebin urls from the yaml file
    :param updatebin_urls_file:
    :return updatebin_urls:
    """
    try:
        with open(updatebin_urls_file, 'r') as stream:
            updatebin_urls = yaml.load(stream)
    except IOError:
        raise AssertionError("Exceptions occurred while reading file %s" % updatebin_urls_file)

    # pull the latest pass build
    if BuiltIn().get_variable_value("${PLATFORM}") is not None:
        platform = BuiltIn().get_variable_value("${PLATFORM}")
    else:
        platform = 'Composer'
    if BuiltIn().get_variable_value("${PULL_LATEST_PASSBUILD}") is not None:
        pull = BuiltIn().get_variable_value("${PULL_LATEST_PASSBUILD}")
    else:
        pull = True
    if pull:
        for k in updatebin_urls.keys():
            if re.search(r'PASS', updatebin_urls[k]):
                tl = updatebin_urls[k].split('/')
                tl.pop(-1)
                url = string.join(tl, '/')
                website = urllib2.urlopen(url)
                html = website.read()
                if k == '50000':
                    pattern = r'HPEOneView-%s-fullupdate-\d*\.\d*\.\d*-\d{7}_PASS\d*.bin' % platform
                    pbs = re.findall('href="(%s)"' % pattern, html)
                else:
                    pattern = r'.*\d*\.\d*\.\d*-\d{7}_PASS\d*.bin'
                    pbs = re.findall('href="(%s)"' % pattern, html)
                pb = sorted(pbs)[-1]
                url = url + '/' + pb
                updatebin_urls[k] = url
    logger._log_to_console_and_log_file("\nupdatebin_urls are \n%s" % updatebin_urls)

    return updatebin_urls


def check_update_hops_files(dir, hops, updatebin_urls):
    """
    Check if update.bin files in update hops exist in dir
    :param dir:
    :param hops:
    :param updatebin_urls:
    """
    check = True
    for hop in hops:
        filename = updatebin_urls[hop].split('/')[-1]
        localfile = os.path.join(dir, filename)
        if not os.path.exists(localfile):
            logger._log_to_console_and_log_file("Missing %s for hop %s" % (filename, hop))
            check = False

    return check


def check_update_hops_urls(hops, updatebin_urls):
    """
    Check if urls for update hops exist in updatebin_urls
    :param hops:
    :param updatebin_urls:
    """
    check = True
    for hop in hops:
        if hop not in updatebin_urls.keys():
            logger._log_to_console_and_log_file("Missing update.bin url for hop %s" % hop)
            check = False

    return check
