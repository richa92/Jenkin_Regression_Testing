from RoboGalaxyLibrary.utilitylib import logging as logger
import re
import subprocess
import platform


class VcsuHelper(object):
    # Helper library to run cpqlocfg utility.

    def run_vcsu(self, command):
        os = platform.system()
        if os == 'Windows':
            try:
                logger._debug("The command is %s " % command)
                output = subprocess.check_output(command)
                logger._debug("The output is %s" % output)
                if 'updated successfully' in output:
                    return output, 'SUCCESS'
                else:
                    return output, 'FAIL'
            except subprocess.CalledProcessError, e:
                return e.output, 'FAIL'
        else:
            return 'vcsu.exe only runs on Windows', 'FAIL'
