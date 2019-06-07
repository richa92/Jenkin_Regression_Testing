"""
setup-helper.py

Helper functions for setup and teardown
"""


def merge_two_dictionaries(d1, d2):
    """ Merge d2 dictionary into d1 using shallow copy. """
    d = d1.copy()
    d.update(d2)
    return d
