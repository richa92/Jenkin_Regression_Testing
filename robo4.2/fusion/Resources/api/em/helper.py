"""
helper functions that are easier to write in python!
"""
import re


def add_brackets_for_latest_curl(curlversion, ipv6):
    """
    This function adds brackets around IPv6+zone for the latest curl versions
    :param curlversion:  a string like '[7, 19, 7]\r\n[root@ci-9cb654980578 ~]#'
    :param ipv6:         a string like 'fe80:0:0:0:4bed:a8f:3e80:a61d%bond0'
    :return:             Returns ipv6 enclosed in brackets if curl version > 7.38.0
    """
    curlversion = re.sub(r'^\[(.*)\]\r\n.*', r'\1', curlversion)
    version = curlversion.split(',')
    version = map(int, version)
    needs_brackets = [7, 38, 0]
    if version >= needs_brackets:
        ipv6 = "[%s]" % ipv6
    return ipv6
