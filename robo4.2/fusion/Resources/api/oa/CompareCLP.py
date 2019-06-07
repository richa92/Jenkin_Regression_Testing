from robot.libraries.BuiltIn import BuiltIn
from RoboGalaxyLibrary.utilitylib import logging as logger
import re


def block_no_keyword_warn():
    pass


class CompareCLP(object):

    def __init__(self):
        self.fusionlib = BuiltIn().get_library_instance('FusionLibrary')

    def do(self, expect, actual, verbose=False):

        def smart_compare(exp, act):

            exp = (re.sub(r'\s*PID\d\d:\s*', '\n', exp, re.MULTILINE)).split('\n')
            act = (re.sub(r'\s*PID\d\d:\s*', '\n', act, re.MULTILINE)).split('\n')

            if verbose:
                print "exp", exp
                print "act", act

            missing = [e for e in exp if (e not in act) and (e is not '')]
            extra = [a for a in act if (a not in exp) and (a != 'diag>')]

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
        actual = re.sub(r'\n.*status:.*\n', '\n', actual)

#        get rid of the stuff from actual up to the first header.  Extra info not compared.
#        for example, the first two lines below.
#	     >>> Blade 1: HP ProLiant BL460c Gen8 <<<
#        Blade 1 mezz F: NOT FOUND
#        --------------------------------------
#        HP FlexFabric 10Gb 2-port 554M Adapter
        firstHeader = actual.index('-----')
        actual = '\n' + actual[firstHeader:]
        expect = re.sub(r'diag>\n', 'diag>', expect)

        if verbose:
            logger._log_to_console_and_log_file("Actual now: %s" % actual)
            logger._log_to_console_and_log_file("Expect now: %s" % expect)
#
#   Start comparing the expected vs the actual
        # if as a string they match, then no need to do a smart compare
        if expect == actual:
            logger._log_to_console_and_log_file("expect == actual.  String equal, no further compare needed.")
            return 1
        else:
            logger._log_to_console_and_log_file("expect != actual, will do smart compare")

        # split into sections.  match '-' line so we don't have a hardcoded length of '-'.
        eListMatchObj = re.search('(-+)', expect)
        aListMatchObj = re.search('(-+)', actual)
        eList = expect.split(eListMatchObj.group(1))
        aList = actual.split(aListMatchObj.group(1))
        logger._log_to_console_and_log_file("Split on: %s into %s sections" % (eListMatchObj.group(1), len(eList) - 1))
        if len(aList) != len(eList):
            logger._log_to_console_and_log_file("aList and eList counts diff.  Problem with split.  a: %s, e: %s" % (len(aList) - 1, len(eList) - 1))
            return 0

        rc = 1
        for i in xrange(1, len(eList)):
            if eList[i] == aList[i]:
                logger._log_to_console_and_log_file("Sections %s are equal." % i)
                if verbose:
                    logger._log_to_console_and_log_file("eList. %s" % eList[i])
                    logger._log_to_console_and_log_file("aList: %s" % aList[i])
            else:
                logger._log_to_console_and_log_file("Section %s requires a smart compare." % i)
                if verbose:
                    logger._log_to_console_and_log_file("eList. %s" % eList[i])
                    logger._log_to_console_and_log_file("aList: %s" % aList[i])

                if "FIP:" in eList[i]:
                    logger._log_to_console_and_log_file("Multiple FIP, split and check each")
                    eFip = eList[i].split('FIP: ')
                    aFip = aList[i].split('FIP: ')

                    for f in xrange(1, len(eFip)):
                        logger._log_to_console_and_log_file("FIP: %s" % (f - 1))
                        if not smart_compare(eFip[f], aFip[f]):
                            rc = 0
                elif not smart_compare(eList[i], aList[i]):
                    rc = 0

        return rc
