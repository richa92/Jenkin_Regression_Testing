#
# Accepts a dict with key that has a list of dict as a value
# top_key is the key to that list.  sort_keys is order in which to sort
#
# dict = {
#    top_key: [
#       {"key1": "x", "key2": "y", "key3", "z"},
#       {"key3": "z", "key1": "x", "key2", "y"}
#    ]
# }
from operator import itemgetter
from RoboGalaxyLibrary.utilitylib import logging as logger


def sort_helper(dict_with_list_of_dict, top_key, sort_keys):
    for key in sort_keys:
        logger._debug("Sort top_key %s by %s" % (top_key, key))
        dict_with_list_of_dict[top_key] = sorted(dict_with_list_of_dict[top_key], key=itemgetter(key))

    return dict_with_list_of_dict
