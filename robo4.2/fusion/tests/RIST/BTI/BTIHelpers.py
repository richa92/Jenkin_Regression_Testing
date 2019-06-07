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


class StorageSize(Enum):
    OneMB = 1048576
    FourMB = 4194304
    TenMB = 10485760
    OneGB = 1073741824
    TwoGB = 2147483648
    FiveGB = 5368709120
    TenGB = 10737418240
    ThirtyGB = 32212254720
    OneFortyTB = 17592186044416


def cleanup_dir(dir):
    """
    Cleanup local dir
    :param dir:
    """
    files = os.listdir(dir)
    for file in files:
        if file.endswith(".bin"):
            os.remove(os.path.join(dir, file))
        if file.endswith(".sdmp"):
            os.remove(os.path.join(dir, file))
        if file.endswith(".gz"):
            os.remove(os.path.join(dir, file))


def download_updatebin_file(dir, url, chunk_size=StorageSize.OneMB.value):
    """
    Download update.bin file from url
    :param dir:
    :param url:
    :param chunk_size: default 10240000
    """
    urllib3.disable_warnings()
    filename = url.split('/')[-1]
    localfile = os.path.join(dir, filename)

    try:
        logger._log_to_console_and_log_file("Downloading file from %s..." % url)
        resp = requests.get(url, stream=True, verify=False)

        with open(localfile, 'wb') as f:
            for chunk in resp.iter_content(chunk_size=chunk_size):
                if chunk:
                    f.write(chunk)
                    f.flush()
        logger._log_to_console_and_log_file("Downloaded file from %s" % url)
        return True

    except Exception as e:
        raise AssertionError("Exceptions occurred while download %s" % url)


def download_updatebin_files(dir, hops, updatebin_urls):
    """
    Download update.bin files
    :param dir:
    :param hops:
    :param updatebin_urls:
    """
    ts = []
    for hop in hops:
        filename = updatebin_urls[hop].split('/')[-1]
        tn = 'download_%s' % filename
        t = threading.Thread(name=tn, target=download_updatebin_file, args=(dir, updatebin_urls[hop],))
        logger._log_to_console_and_log_file("Starting thread %s..." % tn)
        t.start()
        ts.append(t)

    for t in ts:
        t.join()


def get_ova_build(url):
    """
    Get OVA build
    :param url:
    :return build:
    """
    build = re.sub(r'.*_([\d.]*[-_]\d{6,7}).*', r'\1', url)
    # pad extra 0 to match OV software version
    build = re.sub(r'(.*)_(.*)', r'\1_0\2', build).replace('_', '-')
    logger._debug("The OVA build number is %s" % build)

    return build


def get_updatebin_build(updatebin_file):
    """
    Get updatebin file build
    :param updatebin_urls_file:
    :return build:
    """
    # remove SNAPSHOT
    build = updatebin_file.replace('SNAPSHOT-', '')
    build = re.sub(r'.*-([\d.]*-\d{7}).*', r'\1', build)
    logger._debug("The updatebin build number is %s" % build)

    return build


def remove_local_updatebin_files(dir):
    """
    Remove local update.bin files
    :param dir:
    """
    files = os.listdir(dir)
    for file in files:
        if file.endswith(".bin"):
            os.remove(os.path.join(dir, file))


def suppress_warnings_during_appliance_reboot():
    """
    Suppress warnings from urllib3
    """
    fusion_lib = BuiltIn().get_library_instance('FusionLibrary')
    fusion_lib.fusion_client.suppress_urllib3_warnings()
