from robot.libraries.BuiltIn import BuiltIn
from RoboGalaxyLibrary.utilitylib import logging as logger

import re
import Build_data


class Build_Expected_from_Response(object):

    def __init__(self):
        self.fusionlib = BuiltIn().get_library_instance('FusionLibrary')

    def get(self, response, uriCache={}, parentKey="", wordy=False):

        expected = {}
        restTypeWarnings = {}

        def short_name_lookup(rest_type):
            rest_types = Build_data.short_names

            if rest_type in rest_types:
                return rest_types[rest_type]
            else:
                return "TYPE UNKNOWN"

        for key in response.keys():
            if wordy:
                logger._log_to_console_and_log_file("Key : %s" % key)

            if key in Build_data.expected_exclude:
                if parentKey in Build_data.expected_exclude[key] or Build_data.expected_exclude[key] == "":
                    logger._log_to_console_and_log_file("Key to be excluded: %s %s" % (key, parentKey))
                    continue

            if isinstance(response[key], list):
                expected[key] = []
                for i in xrange(0, len(response[key])):
                    if isinstance(response[key][i], dict):
                        sub_dict = self.get(response[key][i], uriCache, key, wordy)
                        expected[key].append(sub_dict)
                    else:
                        miniDict = {"x": response[key][i]}
                        miniDict = self.get(miniDict, uriCache, key, wordy)
                        # need to see if item returned value.  ie. a uri that was able to resolve to name.
                        if "x" in miniDict:
                            expected[key].append(miniDict["x"])
                        else:
                            expected[key] = []

                continue

            if isinstance(response[key], dict):
                sub_dict = self.get(response[key], uriCache, key, wordy)
                expected[key] = sub_dict
                continue

            logger._log_to_console_and_log_file("r : %s" % response[key])
            if isinstance(response[key], str) or isinstance(response[key], unicode):
                matchObj = re.search(r'/rest/(.*?)/', response[key], re.I)
                if matchObj:
                    uri = response[key]

                    if uri in uriCache:
                        if wordy:
                            logger._log_to_console_and_log_file("URI Cache already has %s" % uri)
                            logger._log_to_console_and_log_file("URI Cache name %s" % uriCache[uri])
                        expected[key] = uriCache[uri]
                        continue
                    else:
                        rest_type = matchObj.group(1)
                        shortname = short_name_lookup(rest_type)

                        if shortname == "TYPE UNKNOWN" and rest_type not in restTypeWarnings:
                            logger.warn("Build Expected WARNING: short_name{} doesn't contain rest type: %s" % rest_type)
                            logger.warn("Add to Build_data.py if this rest call should be defined.")
                            logger.warn("")
                            restTypeWarnings[rest_type] = "cached"
                            continue

                        if wordy:
                            logger._log_to_console_and_log_file("Need to get name from URI and build expected: %s" % uri)
                            logger._log_to_console_and_log_file("Type: %s" % rest_type)
                            logger._log_to_console_and_log_file("Short Name: %s" % shortname)

                        resp = self.fusionlib.fusion_api_get_resource(uri)
                        if 'name' in resp:
                            name = resp['name']
                            if shortname == "SHT:":  # need to get adapter info.  Can't just use name as it isn't deterministic
                                #remove index from name:  SY 480 Gen9 2  to SY 480 Gen9
                                name = name[:-2]
                                for adapter in resp['adapters']:
                                    name += (':' + str(adapter['slot']) + ':' + adapter['model'])
                        else:
                            # name = "NAME NOT OBTAINED"
                            logger.warn("Build Expected WARNING: Name for uri not obtained, item to be ignored.  Key: %s, URI: %s" % (key, uri))
                            logger.warn("")
                            continue
                        if wordy:
                            logger._log_to_console_and_log_file("Uri name obtained: %s" % name)

                        # add to uriCache so we don't have to call GET every time
                        uriCache[uri] = (shortname + name)

                        expected[key] = (shortname + name)
                        continue

            # otherwise just copy
            expected[key] = response[key]

        # Some items are conditional.  Try to fix here.  Otherwise user must manually fix.
        for key in expected.keys():
            if key in Build_data.conditional_items:
                if wordy:
                    logger._log_to_console_and_log_file("Found conditional item %s" % key)
                if expected[key] in Build_data.conditional_items[key]:
                    for item in Build_data.conditional_items[key][expected[key]].keys():
                        if (item in expected) and (expected[item] != None):
                            expected[item] = Build_data.conditional_items[key][expected[key]][item]
                            if wordy:
                                logger._log_to_console_and_log_file("Conditional item set to %s" % expected[item])
            # Some items should be expressed as an int range
            for rkey in Build_data.range_items.keys():
                if re.match(rkey, key) and expected[key] != None:
                    if expected[key] in Build_data.cant_range:
                        continue
                    if wordy:
                        msg = "Key: {}, rkey: {}".format(key, rkey)
                        logger._log_to_console_and_log_file("Found matching range_items key %s" % msg)
                    thisExpected = int(expected[key])
                    if thisExpected == 0:
                        logger.warn("Build Expected WARNING: Initial Range value is 0.  Can't build valid range for %s" % key)
                        logger.warn("")
                    epsilon = int(thisExpected * Build_data.range_items[rkey])
                    min = thisExpected - epsilon
                    max = thisExpected + epsilon
                    expected[key] = "RANGE:{}:{}".format(min, max)
                    if wordy:
                        logger._log_to_console_and_log_file("Set to %s" % expected[key])
        return expected
