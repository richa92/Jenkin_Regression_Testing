import time
import os
from functools import wraps
from datetime import datetime
from RoboGalaxyLibrary.utilitylib.logging import logger


def TimeoutChecker(timeout_sec=30, interval_sec=5):
    """ TimeoutChecker
        Description : Function decorator for checking if decorated function return true in specified timeout_sec
    """
    def wrap(f):
        @wraps(f)
        def wrapped_f(*args, **kwargs):
            start_time = datetime.now()
            while True:
                result = f(*args, **kwargs)
                # None indicates immediately exit
                if result is None:
                    return False
                if result is True:
                    return True
                # if reach timeout
                if (datetime.now() - start_time).seconds >= timeout_sec:
                    # self.getLogger().warn("Page not loaded within %s secs!" % timeout_sec)
                    return False
                time.sleep(interval_sec)
        return wrapped_f
    return wrap


def get_ip_count(startip, endip):
    '''
    function to return the no.of ip's in a range given the start and end IP
    '''
    decimalDifference = [int(y) - int(x) for x, y in zip(startip.split('.'), endip.split('.'))]
    ipcount = 0
    for number in decimalDifference:
        ipcount *= 256
        ipcount += number
    return ipcount + 1


def get_firmware_bundle(fw_path, fw_name=''):
    if os.path.exists(fw_path):
        spp_folder = fw_path
    else:
        return False
    spp_list = [each for each in os.listdir(spp_folder) if each.startswith(fw_name)]
    if not spp_list:
        logger.debug("Please upload a SPP to folder '%s' before test" % spp_folder)
        return False
    spp_name = sorted(spp_list, reverse=True)[0]

    absolute_path = spp_folder + '\\' + spp_name
    if not os.path.isfile(absolute_path):
        return False

    return absolute_path


def get_firmware_version_by_file_name(absolute_path):
    fw_name = os.path.basename(absolute_path)
    fw_version = fw_name.rstrip(".iso")

    return fw_version
