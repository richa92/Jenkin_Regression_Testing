from robot.libraries.BuiltIn import BuiltIn
from RoboGalaxyLibrary.utilitylib import logging as logger

import re
import Build_data


class Build_Initial_Template(object):
    def __init__(self):
        self.fusionlib = BuiltIn().get_library_instance('FusionLibrary')

    def get(self, response, wordy=False):

        expected = {}

        for key in response.keys():
            if wordy:
                logger._log_to_console_and_log_file("Key : %s" % key)

            if key in Build_data.template_exclude:
                logger._log_to_console_and_log_file("Key to be excluded: %s" % key)
                continue

            if isinstance(response[key], list):
                expected[key] = []
                # if an empty list then just contine
                if len(response[key]) == 0:
                    continue
                # sort the list as we only add one to the template.  reverse so the item with the most stuff is first
                response[key] = sorted(response[key], reverse=True)
                if isinstance(response[key][0], dict):
                    sub_dict = self.get(response[key][0], wordy)
                    expected[key].append(sub_dict)
                else:
                    miniDict = {"x": response[key][0]}
                    miniDict = self.get(miniDict, wordy)
                    expected[key].append(miniDict["x"])
                # we only need one item, unless they are different but for now just add the first item
                continue

            if isinstance(response[key], dict):
                sub_dict = self.get(response[key], wordy)
                expected[key] = sub_dict
                continue

            # get rid of uri values
            if isinstance(response[key], str) or isinstance(response[key], unicode):
                # matchObj = re.search(r'(/rest/.*)', response[key], re.I)
                # if matchObj:
                #   response[key] = response[key].replace(matchObj.group(1),"")
                response[key] = ""

            if wordy:
                logger._log_to_console_and_log_file("Value: %s" % response[key])

            expected[key] = response[key]

        return expected
