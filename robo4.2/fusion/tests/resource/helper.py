"""
helper functions that are easier to write in python!
"""


def add_brackets_for_latest_curl(curlversion, ipv6):
    """
    This function adds brackets around IPv6+zone for the latest curl versions
    :param curlversion:  This should be a list with 3 integer values in it
    :param ipv6:         This should be an IPv6 address and any zone interface identifier (%bond0)
    :return:             Returns a string enclosed in brackets
    """
    needs_brackets = [7, 38, 0]
    if curlversion >= needs_brackets:
        ipv6 = "[%s]" % ipv6
    return ipv6
