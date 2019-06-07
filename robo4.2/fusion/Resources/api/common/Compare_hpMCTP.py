from robot.libraries.BuiltIn import BuiltIn
from RoboGalaxyLibrary.utilitylib import logging as logger
import re


def block_no_keyword_warn():
    pass


class Compare_hpMCTP(object):

    def __init__(self):
        self.fusionlib = BuiltIn().get_library_instance('FusionLibrary')

    def do(self, expect, actual, verbose=False):

        def smart_compare(exp, act):

            # Remove leading whitespaces
            exp = (re.sub(r'^\s*', '', exp))
            act = (re.sub(r'^\s*', '', act))

            if verbose:
                logger._log_to_console_and_log_file("expected after removing leading white space: %s" % exp)
                logger._log_to_console_and_log_file("actual after removing leading white space: %s" % act)

            missing = [e for e in exp if (e not in act) and (e is not '')]
            extra = [a for a in act if (a not in exp)]

            rc = 1  # True (good, until proven otherwise)
            if extra:
                logger._log_to_console_and_log_file("extra item found: %s" % extra)
                rc = 0
            else:
                logger._log_to_console_and_log_file("No Extra found.")

            if missing:
                logger._log_to_console_and_log_file("missing item: %s" % missing)
                rc = 0
            else:
                logger._log_to_console_and_log_file("No Missing found.")

            return rc

#   Need to delete some items.
        actual = re.sub(r'\n\r', '\n', actual)

#        get rid of the stuff from actual up to the first header.  Extra info not compared.
#        for example, the first three lines below.
#         hpMCTP 2.3.0-4
#         Copyright (c) 2015-2016 Hewlett-Packard - All Rights Reserved
#         -------------------------------------------------------------
#         <ISCSI-Boot-Cats>
        headerEnd = actual.index('<ISCSI-Boot-Cats>')
        actual = '\n' + actual[headerEnd:]

        if verbose:
            logger._log_to_console_and_log_file("Actual now: %s" % actual)
            logger._log_to_console_and_log_file("Expect now: %s" % expect)

#   Start comparing the expected vs the actual
        # if as a string they match, then no need to do a smart compare
        if expect == actual:
            return logger._log_to_console_and_log_file("expect == actual.  String equal, no further compare needed.")

        else:
            logger._log_to_console_and_log_file("expect != actual, will do smart compare")

        # split into single lines.
        eList = expect.split('\n')
        aList = actual.split('\n')
        logger._log_to_console_and_log_file("Split on: %s into %s sections" % ('\n', len(eList) - 1))
        if len(aList) != len(eList):
            errMsg = "aList and eList counts diff.  Problem with split.  a: %s, e: %s" % (len(aList) - 1, len(eList) - 1)
            logger._log_to_console_and_log_file(errMsg)
            raise AssertionError(errMsg)

        for i in xrange(1, len(eList)):
            if eList[i] == aList[i]:
                logger._log_to_console_and_log_file("Sections %s are equal." % i)
                if verbose:
                    logger._log_to_console_and_log_file("expect: %s" % eList[i])
                    logger._log_to_console_and_log_file("actual: %s" % aList[i])
            else:
                logger._log_to_console_and_log_file("Section %s requires a smart compare." % i)
                if verbose:
                    logger._log_to_console_and_log_file("expect: %s" % eList[i])
                    logger._log_to_console_and_log_file("actual: %s" % aList[i])

                if not smart_compare(eList[i], aList[i]):
                    errMsg = "Expected: '%s' does not match '%s'" % (eList[i], aList[i])
                    logger._log_to_console_and_log_file(errMsg)
                    raise AssertionError(errMsg)
