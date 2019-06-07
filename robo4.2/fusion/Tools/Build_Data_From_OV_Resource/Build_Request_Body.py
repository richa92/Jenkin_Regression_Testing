from robot.libraries.BuiltIn import BuiltIn
from RoboGalaxyLibrary.utilitylib import logging as logger

import Build_data


class Build_Request_Body(object):

    def __init__(self):
        self.fusionlib = BuiltIn().get_library_instance('FusionLibrary')

    def get(self, dataDict, uriCache={}, wordy=False):

        requestBody = {}

        def rest_lookup(type):
            lookup = dict(zip(Build_data.short_names.values(), Build_data.short_names.keys()))

            if lookup.has_key(type):
                return lookup[type]
            else:
                return "TYPE UNKNOWN"

        def excluded_item(item):
            excluded_items = {"portId": ""}

            if excluded_items.has_key(item):
                return True
            else:
                return False

        for key in dataDict.keys():
            if wordy:
                logger._log_to_console_and_log_file("Key : %s" % key)

            if isinstance(dataDict[key], list):
                requestBody[key] = []
                for i in xrange(0, len(dataDict[key])):
                    if isinstance(dataDict[key][i], dict):
                        sub_dict = self.get(dataDict[key][i], uriCache, wordy)
                        requestBody[key].append(sub_dict)
                    else:
                        miniDict = {"x": dataDict[key][i]}
                        miniDict = self.get(miniDict, uriCache, wordy)
                        requestBody[key].append(miniDict["x"])
                continue

            if isinstance(dataDict[key], dict):
                sub_dict = self.get(dataDict[key], uriCache, wordy)
                requestBody[key] = sub_dict
                continue

            logger._log_to_console_and_log_file("value : %s" % dataDict[key])
            if (isinstance(dataDict[key], str) or isinstance(dataDict[key], unicode)) and not excluded_item(key):
                words = dataDict[key].split(":")
                # if a name splits into 6 words, then it is probably a mac or 8 words a wwnn name thus don't bother doing a name lookup
                # just ignore anything > 6 and if someone creates a resource name with that many ':', deal with it then
                if len(words) >= 2 and len(words) < 6:
                    resource_type = words[0]
                    name = ":".join(words[1:])

                    rest_path = rest_lookup(resource_type + ":")
                    if rest_path == "TYPE UNKNOWN":
                        logger.warn("Build Request Body WARNING: short_name{} doesn't contain resource type: %s" % resource_type)
                        logger.warn("Extracted from key: %s with value: %s" % (key, dataDict[key]))
                        logger.warn("Add to Build_data.py if this resource type should be defined as a lookup resource.")
                        logger.warn("")
                        requestBody[key] = "UNABLE to resolve: " + dataDict[key]
                        continue

                    uri = "/rest/" + rest_path
                    uri += ('?filter="' + "'name'=='" + name + "'" + '"')

                    if uriCache.has_key(dataDict[key]):
                        if wordy:
                            logger._log_to_console_and_log_file("URI Cache already has %s" % dataDict[key])
                            logger._log_to_console_and_log_file("URI Cache %s" % uriCache[dataDict[key]])
                        requestBody[key] = uriCache[dataDict[key]]
                        continue
                    else:
                        if wordy:
                            logger._log_to_console_and_log_file("Need to get URI from OneView for: %s" % dataDict[key])
                            logger._log_to_console_and_log_file("GET on: %s" % uri)

                        resp = self.fusionlib.fusion_api_get_resource(uri)
                        uri = resp["members"][0]["uri"]
                        if wordy:
                            logger._log_to_console_and_log_file("Uri obtained: %s" % uri)

                        # add to uriCache so we don't have to call GET every time
                        uriCache[dataDict[key]] = uri

                        requestBody[key] = uri
                        continue

            # otherwise just copy
            requestBody[key] = dataDict[key]

            # Some items are conditional.  Try to fix here.  Otherwise user must manually fix.
            for key in requestBody.keys():
                if key in Build_data.conditional_items:
                    if wordy:
                        logger._log_to_console_and_log_file("Found conditional item %s" % key)
                    if requestBody[key] in Build_data.conditional_items[key]:
                        for item in Build_data.conditional_items[key][requestBody[key]].keys():
                            if (item in requestBody) and (requestBody[item] != None):
                                requestBody[item] = ""
                                if wordy:
                                    logger._log_to_console_and_log_file("Conditional item set to ''")

        return requestBody
